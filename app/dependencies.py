from app.database import DatabaseManager
from app.logics import GraphLogic, VEXLogic
from app.services import (
    CWEService,
    ExploitService,
    TIXService,
    VEXService,
    VulnerabilityService,
)
from app.utils import JSONEncoder, RequestContext, SessionPool


class ServiceContainer:
    instance: ServiceContainer | None = None
    db_manager: DatabaseManager | None = None
    cwe_service: CWEService | None = None
    exploit_service: ExploitService | None = None
    tix_service: TIXService | None = None
    vex_service: VEXService | None = None
    vulnerability_service: VulnerabilityService | None = None
    json_encoder: JSONEncoder | None = None
    session_pool: SessionPool | None = None
    request_context: RequestContext | None = None
    graph_logic: GraphLogic | None = None
    vex_logic: VEXLogic | None = None

    def __new__(cls) -> ServiceContainer:
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_db(self) -> DatabaseManager:
        if self.db_manager is None:
            self.db_manager = DatabaseManager()
        return self.db_manager

    def get_cwe_service(self) -> CWEService:
        if self.cwe_service is None:
            self.cwe_service = CWEService(self.get_db())
        return self.cwe_service

    def get_exploit_service(self) -> ExploitService:
        if self.exploit_service is None:
            self.exploit_service = ExploitService(self.get_db())
        return self.exploit_service

    def get_tix_service(self) -> TIXService:
        if self.tix_service is None:
            self.tix_service = TIXService(self.get_db())
        return self.tix_service

    def get_vex_service(self) -> VEXService:
        if self.vex_service is None:
            self.vex_service = VEXService(self.get_db())
        return self.vex_service

    def get_vulnerability_service(self) -> VulnerabilityService:
        if self.vulnerability_service is None:
            self.vulnerability_service = VulnerabilityService(self.get_db())
        return self.vulnerability_service

    def get_json_encoder(self) -> JSONEncoder:
        if self.json_encoder is None:
            self.json_encoder = JSONEncoder()
        return self.json_encoder

    def get_session_pool(self) -> SessionPool:
        if self.session_pool is None:
            self.session_pool = SessionPool()
        return self.session_pool

    def get_request_context(self) -> RequestContext:
        if self.request_context is None:
            self.request_context = RequestContext()
        return self.request_context

    def get_graph_logic(self) -> GraphLogic:
        if self.graph_logic is None:
            self.graph_logic = GraphLogic()
        return self.graph_logic

    def get_vex_logic(self) -> VEXLogic:
        if self.vex_logic is None:
            self.vex_logic = VEXLogic()
        return self.vex_logic


def get_db() -> DatabaseManager:
    return ServiceContainer().get_db()


def get_cwe_service() -> CWEService:
    return ServiceContainer().get_cwe_service()


def get_exploit_service() -> ExploitService:
    return ServiceContainer().get_exploit_service()


def get_tix_service() -> TIXService:
    return ServiceContainer().get_tix_service()


def get_vex_service() -> VEXService:
    return ServiceContainer().get_vex_service()


def get_vulnerability_service() -> VulnerabilityService:
    return ServiceContainer().get_vulnerability_service()


def get_json_encoder() -> JSONEncoder:
    return ServiceContainer().get_json_encoder()


def get_session_pool() -> SessionPool:
    return ServiceContainer().get_session_pool()


def get_request_context() -> RequestContext:
    return ServiceContainer().get_request_context()


def get_graph_logic() -> GraphLogic:
    return ServiceContainer().get_graph_logic()


def get_vex_logic() -> VEXLogic:
    return ServiceContainer().get_vex_logic()
