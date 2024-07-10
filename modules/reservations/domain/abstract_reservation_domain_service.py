import abc
import datetime
from shared.custom_types.entity_id import EntityId
from modules.reservations.shared_kernel.custom_types.reservation_id import ReservationId

class AbstractReservationDomainService(abc.ABC):
    @abc.abstractmethod
    def create_reservation(
        self,
        first_name: str,
        last_name: str,
        depart_date: datetime.date,
        return_date: datetime.date,
    ) -> ReservationId:
        raise NotImplementedError
