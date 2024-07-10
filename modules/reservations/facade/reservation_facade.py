from modules.reservations.facade.abstract_reservation_facade import (
    AbstractReservationFacade,
)
from modules.reservations.domain.abstract_reservation_domain_service import (
    AbstractReservationDomainService,
)
from modules.reservations.shared_kernel.custom_types.reservation_id import ReservationId


class ReservationFacade(AbstractReservationFacade):
    def __init__(
        self, reservation_domain_service: AbstractReservationDomainService
    ) -> None:
        self.reservation_domain_service = reservation_domain_service
        super().__init__()

    def create_reservation(self, create_reservation_body: dict) -> ReservationId:
        reservation_id = self.reservation_domain_service.create_reservation(
            first_name=create_reservation_body["first_name"],
            last_name=create_reservation_body["last_name"],
            depart_date=create_reservation_body["depart_date"],
            return_date=create_reservation_body["return_date"],
        )
        return reservation_id
