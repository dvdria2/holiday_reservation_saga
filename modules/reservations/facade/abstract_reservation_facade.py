import abc
from modules.reservations.shared_kernel.custom_types.reservation_id import ReservationId


class AbstractReservationFacade(abc.ABC):
    @abc.abstractmethod
    def create_reservation(self, create_reservation_body: dict) -> ReservationId:
        raise NotImplementedError
