from fastmcp import FastMCP

from app.tools import (
    get_cwe_tool,
    get_cwes_by_vulnerability_tool,
    get_exploit_tool,
    get_exploits_by_vulnerability_tool,
    get_package_ssc_tool,
    get_package_status_tool,
    get_tixs_tool,
    get_version_ssc_tool,
    get_version_status_tool,
    get_vexs_tool,
    get_vulnerabilities_by_cwe_tool,
    get_vulnerabilities_by_exploit_tool,
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
        "get_package_ssc",
        get_package_ssc_tool,
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
        "get_version_ssc",
        get_version_ssc_tool,
        """
        Use this to check the direct and transitive software supply chain of a version in the dependency graph of the overall software supply chain.
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
        "get_vulnerabilities_by_cwe",
        get_vulnerabilities_by_cwe_tool,
        """
        Use this to get the information of a vulnerabilities related to a CWE by the CWE-ID.
        Input:
            cwe_id: The ID of the CWE to look for.
        """
    ),
    (
        "get_vulnerabilities_by_exploit",
        get_vulnerabilities_by_exploit_tool,
        """
        Use this to get the information of a vulnerabilities related to a exploit by the exploit ID.
        Input:
            exploit_id: The ID of the exploit to look for.
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
        "get_exploits_by_vulnerability_id",
        get_exploits_by_vulnerability_tool,
        """
        Use this to get the information of exploits related to a vulnerability ID.
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
    (
        "get_cwes_by_vulnerability_id",
        get_cwes_by_vulnerability_tool,
        """
        Use this to get the information of CWEs related to a vulnerability ID.
        Input:
            vulnerability_id: The ID of the vulnerability to look for associated cwes.
        """
    ),
    (
        "get_vexs",
        get_vexs_tool,
        """
        Use this to get the Vulnerability Exploitability eXchanges (VEXs) for a given repository owner and name.
        Input:
            owner: The owner of the repository.
            name: The name of the repository.
            sbom_name: The name of the SBOM file.
        """
    ),
    (
        "get_tixs",
        get_tixs_tool,
        """
        Use this to get the Threat Intelligence eXchanges (TIXs) for a given repository owner and name.
        Input:
            owner: The owner of the repository.
            name: The name of the repository.
            sbom_name: The name of the SBOM file.
        """
    )
]

for name, func, description in TOOL_SPECS:
    mcp.tool(name=name, description=description)(func)
