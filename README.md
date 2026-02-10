# Secure Chain MCP Server

[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Lint & Test](https://github.com/securechaindev/securechain-mcp-server/actions/workflows/lint-test.yml/badge.svg)]()
[![GHCR](https://img.shields.io/badge/GHCR-securechain--mcp-blue?logo=docker)](https://github.com/orgs/securechaindev/packages/container/package/securechain-mcp)

An MCP server that provides tools for checking the status of your software supply chain within the context of Secure Chain.

### Key Features

- 🔍 **Multi-ecosystem support:** Query packages from PyPI, NPM, Maven, Cargo, RubyGems, and NuGet ecosystems
- 🛡️ **Vulnerability intelligence:** Access detailed vulnerability, exploit, and CWE information
- 📊 **Supply chain analysis:** Explore direct and transitive dependencies in the software supply chain graph
- 📋 **VEX support:** Retrieve Vulnerability Exploitability eXchange documents for repositories
- ⚡ **MCP integration:** Seamlessly integrates with AI agents and LLMs via Model Context Protocol

## Development requirements

1. [Docker](https://www.docker.com/) to deploy the tool.
2. [Docker Compose](https://docs.docker.com/compose/) for container orchestration.
3. It is recommended to use a GUI such as [MongoDB Compass](https://www.mongodb.com/en/products/compass).
4. The Neo4J browser interface to visualize the graph built from the data is in [localhost:7474](http://0.0.0.0:7474/browser/) when the container is running.
5. Python 3.14 or higher.

## Use Secure Chain MCP with VSCode

### 1. Register on Secure Chain

Go to [Secure Chain](https://securechain.dev/) official lading page, and register yourself as a user.

### 2. Add mcp configuration

Finally, inside the folder `.vscode` add the file `mcp.json` with the next configuration, and start the mcp server:
```json
{
  "servers": {
    "Secure Chain MCP Server": {
      "type": "http",
      "url": "https://mcp.securechain.dev/mcp",
      "headers": {
        "X-Auth-Email": "your_email",
        "X-Auth-Pass": "your_super_secret_password"
      }
    }
  }
}
```

## Deployment with docker

### 1. Clone the repository

Clone the repository from the official GitHub repository:

```bash
git clone https://github.com/securechaindev/securechain-mcp-server.git
cd securechain-mcp-server
```

### 2. Configure environment variables

Create a `.env.local` file from the `.env.example` file and place it in the root directory.

#### Get API Keys

- How to get a _GitHub_ [API key](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

- Modify the **Json Web Token (JWT)** secret key and algorithm with your own. You can generate your own secret key with the command **openssl rand -base64 32**.

### 3. Create Docker network

Ensure you have the `securechain` Docker network created. If not, create it with:

```bash
docker network create securechain
```

### 4. Databases containers

For graphs and vulnerabilities information you need to download the zipped [data dumps](https://doi.org/10.5281/zenodo.16739080) from Zenodo. Once you have unzipped the dumps, inside the root folder run the command:

```bash
docker compose up --build
```

The containerized databases will also be seeded automatically.

### 5. Start the application

Run the command from the project root:

```bash
docker compose -f dev/docker-compose.yml up --build
```

### 6. Create a User in Secure Chain local deployment

Go [here](http://localhost:8000/docs#/Secure%20Chain%20Auth%20-%20User/signup_signup_post) and create an user, for example:

```json
{
  "email": "mcp-bot@example.com",
  "password": "supersecre3T*"
}
```

### 7. Configure the MCP with VSCode

Inside the folder `.vscode/` add the file `mcp.json` with this template:

```json
{
  "servers": {
    "Secure Chain MCP Server": {
      "type": "http",
      "url": "http://localhost:8005/mcp",
      "headers": {
        "X-Auth-Email": "mcp-bot@example.com",
        "X-Auth-Pass": "supersecre3T*"
      }
    }
  }
}
```

And then start the MCP server and begin use it with Copilot for example.

## Python Environment

The project uses Python 3.14 and [uv](https://github.com/astral-sh/uv) as the package manager for faster and more reliable dependency management.

### Setting up the development environment with uv

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Activate the virtual environment** (uv creates it automatically):
   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

## Code Quality

```bash
# Install linter
uv sync --extra dev

# Linting
uv run ruff check app/

# Formatting
uv run ruff format app/
```

## Contributing

Pull requests are welcome! To contribute follow this [guidelines](https://securechaindev.github.io/contributing.html).

## License

[GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.html)

## Links

- [Secure Chain Team](mailto:hi@securechain.dev)
- [Secure Chain Organization](https://github.com/securechaindev)
- [Secure Chain Documentation](https://securechaindev.github.io/)
