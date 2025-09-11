from fastmcp import FastMCP

from app.tools import (
    get_cwe_tool,
    get_exploit_tool,
    get_exploits_by_vuln_id,
    get_package_scc_tool,
    get_package_status_tool,
    get_version_status_tool,
    get_vulnerability_tool,
)

mcp = FastMCP("Secure Chain MCP Tool")

TOOL_SPECS = [
    (
        "get_package_status",
        get_package_status_tool,
        """
        Use this to check if a package exists and get its status in the dependency graph.
        Input:
            node_type: Type of node (PyPIPackage, NPMPackage, MavenPackage, CargoPackage, RubyGemsPackage, NuGetPackage).
            package_name: Name of the package.
        """
    ),
    (
        "get_package_scc",
        get_package_scc_tool,
        """
        Use this to check the direct and transitive software supply chain of a package in the dependency graph of the overall software supply chain.
        Input:
            node_type: Type of node (PyPIPackage, NPMPackage, MavenPackage, CargoPackage, RubyGemsPackage, NuGetPackage).
            package_name: Name of the package.
        """
    ),
    (
        "get_version_status",
        get_version_status_tool,
        """
        Use this to get the status of a specific version of a package in the dependency graph.
        Input:
            node_type: Type of node (PyPIPackage, NPMPackage, MavenPackage, CargoPackage, RubyGemsPackage, NuGetPackage).
            package_name: Name of the package.
            version_name: Name of the version.
        """
    ),
    (
        "get_vulnerability",
        get_vulnerability_tool,
        """
        Use this to get the information of a vulnerability by the ID.
        Input:
            vulnerability_id: The ID of the vulnerability to look for.
        """
    ),
    (
        "get_exploit",
        get_exploit_tool,
        """
        Use this to get the information of an exploit by the ID.
        Input:
            exploit_id: The ID of the exploit to look for.
        """
    ),
    (
        "get_exploits_by_vuln_id",
        get_exploits_by_vuln_id,
        """
        Use this to get the information of exploits by a vulnerability ID.
        Input:
            vulnerability_id: The ID of the vulnerability to look for associated exploits.
        """
    ),
    (
        "get_cwe",
        get_cwe_tool,
        """
        Use this to get the information of a CWE by the ID.
        Input:
            cwe_id: The ID of the CWE to look for.
        """
    ),
]

for name, func, description in TOOL_SPECS:
    mcp.tool(name=name, description=description)(func)
