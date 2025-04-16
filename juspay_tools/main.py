import click
import os
import uvicorn
import dotenv

from starlette.applications import Starlette
from starlette.routing import Mount, Route
from mcp.server.sse import SseServerTransport
from juspay_tools.tools import app

# Load environment variables.
dotenv.load_dotenv()

@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind the server to.")
@click.option("--port", default=8000, type=int, help="Port to listen on for SSE.")
def main(host: str, port: int):
    """Runs the MCP server using HTTP/SSE."""
    
    # Define endpoint paths.
    message_endpoint_path = "/messages/"
    sse_endpoint_path = "/sse"
    
    # Create the SSE transport handler.
    sse_transport_handler = SseServerTransport(message_endpoint_path)
    
    async def handle_sse_connection(request):
        """Handles a single client SSE connection and runs the MCP session."""
        print(f"New SSE connection from: {request.client}")
        
        async with sse_transport_handler.connect_sse(
            request.scope, request.receive, request._send
        ) as streams:
            print(f"MCP Session starting for {request.client}")
            try:
                await app.run(
                    streams[0],
                    streams[1],
                    app.create_initialization_options()
                )
            except Exception as e:
                print(f"Error during MCP session for {request.client}: {e}")
            finally:
                print(f"MCP Session ended for {request.client}")

    # Create a Starlette application with the desired routes.
    starlette_app = Starlette(
        debug=True,
        routes=[
            Route(sse_endpoint_path, endpoint=handle_sse_connection),
            Mount(message_endpoint_path, app=sse_transport_handler.handle_post_message),
        ],
    )

    print(f"Starting MCP server on http://{host}:{port}{sse_endpoint_path}")
    uvicorn.run(starlette_app, host=host, port=port)

if __name__ == "__main__":
    main()