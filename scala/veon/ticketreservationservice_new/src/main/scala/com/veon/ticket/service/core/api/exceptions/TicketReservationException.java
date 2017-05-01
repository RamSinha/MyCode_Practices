
package com.veon.ticket.service.core.api.exceptions;


public class TicketReservationException extends RuntimeException {

    private static final long serialVersionUID = 8988288514170436716L;

    public TicketReservationException(final String message) {
        super(message);
    }
}
