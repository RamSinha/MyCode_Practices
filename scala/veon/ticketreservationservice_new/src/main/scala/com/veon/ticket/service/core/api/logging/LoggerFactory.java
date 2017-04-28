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

package com.veon.ticket.service.core.api.logging;

import org.slf4j.Logger;
import org.slf4j.MDC;

import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

public class LoggerFactory {

    static {
        Path ccvLogPath = Paths.get("/Users/ramsinha", "ticketreservationapi", "log");
        System.setProperty("loghome", ccvLogPath.toString() + File.separator);
        System.setProperty("logname", "apiserver");
        String hostname = System.getProperty("hostname", "INVALID_HOSTNAME");
        MDC.put("hostname", hostname);


        final String jvmIdentifier = System.getProperty("jvmidentifier", "INVALID_JVM_IDENTIFIER");
        MDC.put("jvm_id", jvmIdentifier);
    }

    public static void initialize() {
    }

    public static Logger getLogger(String name) {
        return org.slf4j.LoggerFactory.getLogger(name);
    }
}