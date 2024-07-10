from shared.abstract_repository import AbstractRepository
from shared.custom_types.entity_id import EntityId
from modules.reservations.domain.entities.reservation import Reservation
from modules.reservations.domain.abstract_reservation_domain_service import (
    AbstractReservationDomainService,
)
from modules.reservations.shared_kernel.custom_types.reservation_id import ReservationId
import datetime
import uuid


class ReservationDomainService(AbstractReservationDomainService):
    def __init__(self, repository: AbstractRepository) -> None:
        self.repository = repository

    def create_reservation(
        self,
        first_name: str,
        last_name: str,
        depart_date: datetime.date,
        return_date: datetime.date,
    ) -> ReservationId:
        aggregate = Reservation(
            reservation_id=uuid.uuid4(),
            first_name=first_name,
            last_name=last_name,
            depart_date=depart_date,
            return_date=return_date,
        )
        self.repository.insert(aggregate)
        return aggregate.reservation_id
