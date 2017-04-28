package com.veon.ticket.service.core.api.exceptions;

public class TicketReservationBadRequestException extends RuntimeException{

    private static final long serialVersionUID = 8988288514170436722L;

    public TicketReservationBadRequestException(final String message)
    {
        super(message);
    }
}
