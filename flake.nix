{
  description = "Flake for Juspay-mcp python project.";
  # TODO: Split in multiple files.

  outputs =
    inputs@{ flake-parts, uv2nix, pyproject-nix, pyproject-build-systems, git-hooks, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import inputs.systems;
      imports = [
        (git-hooks + /flake-module.nix)
      ];
      perSystem =
        { self', config, pkgs, ... }:
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
          pre-commit.settings.hooks.nixpkgs-fmt.enable = true;
          packages.default = pythonSet.mkVirtualEnv "juspay-mcp" workspace.deps.all;
          apps.default = {
            type = "app";
            program = "${self'.packages.default}/bin/juspay-mcp";
          };
          packages.test = python.withPackages (ps: with ps; [ pytest ]);
          apps.test = {
            type = "app";
            program = "${self'.packages.test}/bin/pytest";
          };
          devShells.default = self'.devShells.uv2nix;
          devShells.uv2nix = pkgs.mkShell {
            inputsFrom = [
              config.pre-commit.devShell
            ];
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

    git-hooks.url = "github:cachix/git-hooks.nix";
    git-hooks.flake = false;

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
