from shared.entities.aggregate_root import AggregateRoot
from modules.reservations.shared_kernel.custom_types.reservation_id import ReservationId
import datetime

class Reservation(AggregateRoot):
    reservation_id: ReservationId
    first_name: str
    last_name: str
    depart_date: datetime.date
    return_date: datetime.date

