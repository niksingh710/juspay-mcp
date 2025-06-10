{
  description = "Flake for Juspay-mcp python project.";

  outputs =
    inputs@{
      flake-parts,
      uv2nix,
      pyproject-nix,
      pyproject-build-systems,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import inputs.systems;
      perSystem =
        {
          self',
          pkgs,
          ...
        }:
        let
          inherit (pkgs) lib;
          python = pkgs.python313;
          workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
          overlay = workspace.mkPyprojectOverlay { sourcePreference = "wheel"; };
          editableOverlay = workspace.mkEditablePyprojectOverlay { root = "$REPO_ROOT"; };

          pythonSet =
            (pkgs.callPackage pyproject-nix.build.packages {
              inherit python;
            }).overrideScope
              (
                lib.composeManyExtensions [
                  pyproject-build-systems.overlays.default
                  overlay
                ]
              );

          editablePythonSet = pythonSet.overrideScope (
            lib.composeManyExtensions [
              pyproject-build-systems.overlays.default
              overlay
              editableOverlay

              (final: prev: {
                juspay-mcp = prev.juspay-mcp.overrideAttrs (old: {
                  src = lib.fileset.toSource {
                    root = old.src;
                    fileset = lib.fileset.unions [
                      (old.src + "/pyproject.toml")
                      (old.src + "/README.md")
                      (old.src + "/juspay_mcp")
                      (old.src + "/juspay_dashboard_mcp")
                    ];
                  };
                  nativeBuildInputs =
                    old.nativeBuildInputs
                    ++ final.resolveBuildSystem {
                      editables = [ ];
                    };
                });

              })
            ]
          );
          venv = editablePythonSet.mkVirtualEnv "juspay-mcp" workspace.deps.all;
        in
        {
          packages.default = pythonSet.mkVirtualEnv "juspay-mcp" workspace.deps.all;
          apps.default = {
            type = "app";
            program = "${self'.packages.default}/bin/juspay-mcp";
          };
          devShells.default = self'.devShells.uv2nix;
          devShells.uv2nix = pkgs.mkShell {
            packages = [
              venv
              pkgs.uv
            ];
            env = {
              UV_NO_SYNC = "1";
              UV_PYTHON = "${venv}/bin/python";
              UV_PYTHON_DOWNLOADS = "never";
            };

            shellHook = # sh
              ''
                unset PYTHONPATH
                export REPO_ROOT="$(git rev-parse --show-toplevel)"
                export PYTHONPATH="$REPO_ROOT"
              '';
          };
        };
    };

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default";

    pyproject-nix.url = "github:pyproject-nix/pyproject.nix";
    pyproject-nix.inputs.nixpkgs.follows = "nixpkgs";

    uv2nix.url = "github:pyproject-nix/uv2nix";
    uv2nix.inputs.pyproject-nix.follows = "pyproject-nix";
    uv2nix.inputs.nixpkgs.follows = "nixpkgs";

    pyproject-build-systems.url = "github:pyproject-nix/build-system-pkgs";
    pyproject-build-systems.inputs.pyproject-nix.follows = "pyproject-nix";
    pyproject-build-systems.inputs.uv2nix.follows = "uv2nix";
    pyproject-build-systems.inputs.nixpkgs.follows = "nixpkgs";
  };

}
