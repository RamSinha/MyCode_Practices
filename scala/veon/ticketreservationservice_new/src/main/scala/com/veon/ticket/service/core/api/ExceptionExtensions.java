package com.veon.ticket.service.core.api;

import org.apache.commons.lang3.exception.ExceptionUtils;

public class ExceptionExtensions {
    public static String getExceptionMessageWithStackTraceFor(final Throwable throwable) {
        if (throwable == null)
            return "null";

        return String.format(
                "Exception : %s. Stack trace : %s",
                throwable.getMessage(),
                ExceptionUtils.getStackTrace(throwable));
    }
}
