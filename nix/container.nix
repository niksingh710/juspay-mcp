{ inputs, ... }:
{
  perSystem = { pkgs, self', lib, ... }:
    let
      n2c = inputs.nix2container.packages.${pkgs.system}.nix2container;
      default = {
        # Parallel of `Dockerfile`
        name = "juspay-mcp";
        tag = "latest";
        config = {
          Env = [
            "PYTHONUNBUFFERED=1"
          ];
          Entrypoint = [ "${lib.getExe' self'.packages.default "juspay-mcp"}" ];
        };
      };
      sse = default // {
        # Parallel of Dockerfile.sse
        config = default.config // {
          ExposedPorts = {
            "8000/tcp" = { };
          };
        };
      };
      dashboard = default // {
        # Parallel of Dockerfile.dashboard
        config = default.config // {
          Env = default.config.Env ++ [ "JUSPAY_MCP_TYPE=DASHBOARD" ];
        };
      };
      dashboard-sse = dashboard // {
        # Parallel of Dockerfile.dashboard-sse
        config = dashboard.config // {
          ExposedPorts = {
            "8000/tcp" = { };
          };
          # FIXME: Once `@ag` confirms the EntryPoint it is good to go
        };
      };
    in
    {
      packages = {
        docker = n2c.buildImage default;
        docker-sse = n2c.buildImage sse;


        # Use `docker run -it <image-name:hash>`
        # For local running
        # Without `-it` flag the process will terminate instantly
        docker-dashboard = n2c.buildImage dashboard;
        docker-dashboard-sse = n2c.buildImage dashboard-sse;
      };
    };
}
