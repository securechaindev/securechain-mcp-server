# CLAUDE.md - Secure Chain MCP Server

> ⚠️ **IMPORTANTE**: Este archivo NO debe sobrepasar las 500 líneas. Debe contener únicamente información contextual relevante para sesiones de agentes de IA. Mantener conciso y actualizado.

---

## Descripción del Proyecto

**Secure Chain MCP Server** es un servidor MCP (Model Context Protocol) que proporciona herramientas para verificar el estado de la cadena de suministro de software (Software Supply Chain - SSC). Permite a LLMs y agentes de IA consultar información sobre vulnerabilidades, exploits, CWEs y dependencias de paquetes.

- **Versión**: 1.1.0
- **Licencia**: GPL-3.0-or-later
- **Python requerido**: >= 3.14
- **Framework**: FastAPI + FastMCP

---

## Estructura del Proyecto

```
securechain-mcp-server/
├── app/                    # Código fuente principal
│   ├── main.py             # Punto de entrada FastAPI
│   ├── mcp_server.py       # Definición de herramientas MCP
│   ├── settings.py         # Configuración (Pydantic Settings)
│   ├── database.py         # Manager de conexiones (MongoDB + Neo4j)
│   ├── middleware.py       # Middleware de contexto de request
│   ├── dependencies.py     # Inyección de dependencias
│   ├── logger.py           # Configuración de logging
│   ├── exceptions/         # Excepciones personalizadas
│   ├── logics/             # Lógica de negocio
│   │   ├── graph_logic.py  # Operaciones sobre el grafo
│   │   └── vex_logic.py    # Operaciones VEX
│   ├── services/           # Servicios de datos (MongoDB)
│   │   ├── cwe_service.py
│   │   ├── exploit_service.py
│   │   ├── tix_service.py
│   │   ├── vex_service.py
│   │   └── vulnerability_service.py
│   ├── tools/              # Herramientas MCP expuestas
│   │   ├── cwe_tool.py
│   │   ├── exploit_tool.py
│   │   ├── graph_tool.py
│   │   ├── vex_tool.py
│   │   └── vulnerability_tool.py
│   └── utils/              # Utilidades
│       ├── json_encoder.py
│       ├── request_context.py
│       ├── session_manager.py
│       └── session_pool.py
├── dev/                    # Configuración de desarrollo
│   ├── docker-compose.yml
│   └── Dockerfile
├── pyproject.toml          # Configuración del proyecto Python
├── template.env            # Plantilla de variables de entorno
└── Dockerfile              # Dockerfile de producción
```

---

## Bases de Datos

### Neo4j (Grafo de Dependencias)
- **URI**: `bolt://neo4j:7687`
- **Propósito**: Almacena el grafo de dependencias de paquetes
- **Tipos de nodos soportados**:
  - `PyPIPackage` - Paquetes Python
  - `NPMPackage` - Paquetes NPM
  - `MavenPackage` - Paquetes Maven (Java)
  - `CargoPackage` - Paquetes Cargo (Rust)
  - `RubyGemsPackage` - Gemas Ruby
  - `NuGetPackage` - Paquetes NuGet (.NET)

### MongoDB (Vulnerabilidades y Metadatos)
- **URI**: `mongodb://mongoSecureChain:mongoSecureChain@mongo:27017/admin`
- **Bases de datos**:
  - `securechain`: VEXs, TIXs
  - `vulnerabilities`: Vulnerabilidades, CWEs, Exploits
- **Colecciones principales**:
  - `vexs` - Vulnerability Exploitability eXchange
  - `tixs` - Threat Intelligence eXchange
  - `vulnerabilities` - Información de vulnerabilidades
  - `cwes` - Common Weakness Enumeration
  - `exploits` - Exploits conocidos

---

## Herramientas MCP Disponibles

Las herramientas se definen en `app/mcp_server.py` y se implementan en `app/tools/`:

| Herramienta | Descripción |
|-------------|-------------|
| `get_package_status` | Estado de un paquete en el grafo |
| `get_package_ssc` | Cadena de suministro directa/transitiva de un paquete |
| `get_version_status` | Estado de una versión específica |
| `get_version_ssc` | Cadena de suministro de una versión |
| `get_vulnerability` | Información de una vulnerabilidad por ID |
| `get_vulnerabilities_by_cwe` | Vulnerabilidades relacionadas a un CWE |
| `get_vulnerabilities_by_exploit` | Vulnerabilidades relacionadas a un exploit |
| `get_exploit` | Información de un exploit por ID |
| `get_exploits_by_vulnerability_id` | Exploits asociados a una vulnerabilidad |
| `get_cwe` | Información de un CWE por ID |
| `get_cwes_by_vulnerability_id` | CWEs asociados a una vulnerabilidad |
| `get_vexs` | VEXs para un repositorio dado |

---

## Arquitectura y Patrones

### Patrón de Capas
```
Tools (MCP) → Logics → Services → Database
```

- **Tools**: Exponen funcionalidad al MCP, manejan serialización y errores
- **Logics**: Contienen lógica de negocio, llaman al backend o servicios
- **Services**: Acceso directo a MongoDB
- **Database**: Manager singleton para conexiones

### Inyección de Dependencias
Las dependencias se obtienen via `app/dependencies.py`:
```python
from app.dependencies import (
    get_session_pool,
    get_graph_logic,
    get_json_encoder,
    get_request_context,
)
```

### Manejo de Sesiones
- `SessionPool`: Pool de sesiones HTTP por API key
- `SessionManager`: Gestiona sesiones individuales con headers de autenticación
- `RequestContext`: Contexto de request usando `contextvars`

### Middleware
`RequestContextMiddleware` extrae headers de autenticación (`X-Auth-Email`, `X-Auth-Pass`) y los almacena en el contexto del request.

---

## Dependencias Principales

```toml
fastapi==0.122.0        # Framework web
uvicorn==0.38.0         # Servidor ASGI
mcp==1.22.0             # Model Context Protocol
fastmcp==2.13.1         # FastMCP para definir herramientas
pymongo==4.15.4         # Cliente MongoDB async
neo4j==6.0.3            # Driver Neo4j async
pydantic-settings==2.12.0  # Configuración con Pydantic
aiohttp==3.13.2         # Cliente HTTP async
```

---

## Comandos de Desarrollo

### Iniciar en desarrollo
```bash
# Levantar bases de datos
docker compose up --build

# Levantar servidor MCP
docker compose -f dev/docker-compose.yml up --build
```

### Linting
```bash
ruff check app/
ruff format app/
```

### Tests
```bash
pytest                          # Ejecutar tests
pytest --cov=app               # Con cobertura
pytest -v -k "test_name"       # Test específico
```

---

## Variables de Entorno Importantes

| Variable | Descripción | Default |
|----------|-------------|---------|
| `GRAPH_DB_URI` | URI de Neo4j | `bolt://neo4j:7687` |
| `VULN_DB_URI` | URI de MongoDB | (ver template.env) |
| `GRAPH_DB_USER` | Usuario Neo4j | `neo4j` |
| `GRAPH_DB_PASSWORD` | Password Neo4j | `neoSecureChain` |
| `BACKEND_URL` | URL del backend gateway | `http://securechain-gateway:8000` |
| `REQUEST_TIMEOUT` | Timeout de requests HTTP | `60` |
| `DOCS_URL` | URL de documentación | `/docs` |

---

## Endpoints

- **MCP**: `/mcp` - Endpoint principal del servidor MCP
- **Health**: `/health` - Health check
- **Docs**: `/docs` - Swagger UI (configurable)

---

## Excepciones Personalizadas

Ubicadas en `app/exceptions/`:
- `AuthenticationErrorException`
- `PackageNotFoundException`
- `VersionNotFoundException`
- `VulnerabilityNotFoundException` / `VulnerabilitiesNotFoundException`
- `ExploitNotFoundException` / `ExploitsNotFoundException`
- `CWENotFoundException` / `CWEsNotFoundException`
- `VEXsNotFoundException`
- `TIXsNotFoundException`

---

## Configuración MCP para VSCode

Archivo `.vscode/mcp.json`:
```json
{
  "servers": {
    "Secure Chain MCP Server": {
      "type": "http",
      "url": "http://localhost:8005/mcp",
      "headers": {
        "X-Auth-Email": "usuario@ejemplo.com",
        "X-Auth-Pass": "contraseña"
      }
    }
  }
}
```

---

## Convenciones de Código

1. **Async/Await**: Todo el código es asíncrono
2. **Type Hints**: Usar tipado estricto en todas las funciones
3. **Docstrings**: Usar docstrings descriptivos para herramientas MCP
4. **Excepciones**: Lanzar excepciones específicas del dominio
5. **Logging**: Usar `app.logger.logger` para logging

---

## Flujo de una Herramienta MCP

1. Request llega con headers de autenticación
2. Middleware extrae y almacena credenciales en `RequestContext`
3. Herramienta obtiene `api_key` del contexto
4. Se obtiene/crea `SessionManager` del pool
5. Lógica ejecuta operación (API call o query DB)
6. Resultado se serializa con `JSONEncoder`
7. Se retorna `TextContent` al cliente MCP

---

## Links Útiles

- **Organización**: https://github.com/securechaindev
- **Documentación**: https://securechaindev.github.io/
- **Contacto**: hi@securechain.dev
- **Secure Chain Web**: https://securechain.dev/
