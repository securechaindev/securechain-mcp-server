# Secure Chain MCP Server

An MCP server that provides tools for checking the status of your software supply chain within the context of Secure Chain.

## Development requirements

1. [Docker](https://www.docker.com/) to deploy the tool.
2. [Docker Compose](https://docs.docker.com/compose/) for container orchestration.
3. It is recommended to use a GUI such as [MongoDB Compass](https://www.mongodb.com/en/products/compass).
4. The Neo4J browser interface to visualize the graph built from the data is in [localhost:7474](http://0.0.0.0:7474/browser/) when the container is running.
5. Python 3.13 or higher.

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

For graphs and vulnerabilities information you need to download the zipped [data dumps](https://doi.org/10.5281/zenodo.16739081) from Zenodo. Once you have unzipped the dumps, inside the root folder run the command:

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
    "Secure Chain": {
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
The project uses Python 3.13 and the dependencies are listed in `requirements.txt`.

### Setting up the development environment

1. **Create a virtual environment**:
   ```bash
   python3.13 -m venv depex-env
   ```

2. **Activate the virtual environment**:
   ```bash
   source depex-env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.html)

## Links

- [Secure Chain Team](mailto:hi@securechain.dev)
- [Secure Chain Organization](https://github.com/securechaindev)
- [Secure Chain Documentation](https://securechaindev.github.io/)