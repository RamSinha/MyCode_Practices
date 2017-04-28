package com.veon.ticket.service.core.api.logging;
/*
 * ************************************************************************
 *  ADOBE CONFIDENTIAL
 *  ___________________
 *
 *   Copyright 2014 Adobe Systems Incorporated
 *   All Rights Reserved.
 *
 *  NOTICE:  All information contained herein is, and remains
 *  the property of Adobe Systems Incorporated and its suppliers,
 *  if any.  The intellectual and technical concepts contained
 *  herein are proprietary to Adobe Systems Incorporated and its
 *  suppliers and are protected by all applicable intellectual property
 *  laws, including trade secret and copyright laws.
 *  Dissemination of this information or reproduction of this material
 *  is strictly forbidden unless prior written permission is obtained
 *  from Adobe Systems Incorporated.
 * ************************************************************************
 */

import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import net.minidev.json.JSONStyle;
import org.apache.log4j.Layout;
import org.apache.log4j.helpers.ISO8601DateFormat;
import org.apache.log4j.spi.LoggingEvent;
import org.apache.log4j.spi.ThrowableInformation;

import java.text.DateFormat;
import java.util.Date;

public class JSONLayout extends Layout {

    public void activateOptions() {
    }

    @Override
    public String format(LoggingEvent event) {

        DateFormat dformat = new ISO8601DateFormat();

        JSONObject json = new JSONObject();
        json.put("timestamp", dformat.format(new Date(event.getTimeStamp())));
        json.put("hostname", event.getMDC("hostname"));
        json.put("level", event.getLevel().toString());
        json.put("logger", event.getLoggerName());
        json.put("thread", event.getThreadName());
        json.put("message", event.getMessage());
        json.put("job_id", event.getMDC("job_id"));
        json.put("jvm_id", event.getMDC("jvm_id"));

        final String xRequestId = (String) event.getMDC("X-Request-Id");
        if (xRequestId != null && !xRequestId.isEmpty())
            json.put("X-Request-Id", xRequestId);

        ThrowableInformation throwInfo = event.getThrowableInformation();
        if (throwInfo != null) {
            JSONArray excs = new JSONArray();
            String[] excStr = event.getThrowableStrRep();
            if (excStr != null & excStr.length > 0) {
                for (String excMsg : excStr)
                    excs.add(excMsg);
            }

            JSONObject throwJsonObj = new JSONObject();
            throwJsonObj.put("class", throwInfo.getThrowable().getClass().getCanonicalName());
            throwJsonObj.put("stacktrace", excs);
            throwJsonObj.put("exception_message", throwInfo.getThrowable().getMessage());
            json.put("exception", throwJsonObj);
        }

        return json.toJSONString(JSONStyle.NO_COMPRESS) + System.getProperty("line.separator");
    }

    @Override
    public boolean ignoresThrowable() {
        return false;
    }

}

