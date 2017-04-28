package com.veon.ticket.service.core.api.exceptions;

public class TicketReservationPostgresException extends  RuntimeException {

    private static final long serialVersionUID = 8988288514170436721L;

    public TicketReservationPostgresException(final String message)
    {
        super(message);
    }
}