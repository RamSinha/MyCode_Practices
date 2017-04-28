
package com.veon.ticket.service.core.api.javaapi;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.HashMap;

public class JsonMapper {

    JsonFactory factory;
    public ObjectMapper mapper;
    TypeReference<HashMap<String, Object>> typeRef;

    public JsonMapper() {
        this.factory = new JsonFactory();
        this.mapper = new ObjectMapper(factory);
        this.typeRef = new TypeReference<HashMap<String, Object>>() {
        };
    }

    public HashMap<String, Object> toMap(String jsonString) throws IOException {
        // TODO: Catch Jackson exceptions
        try {
            return this.mapper.readValue(jsonString, typeRef);
        } catch (Exception e) {
            throw e;
        }
    }

    public String toJson(Object obj) throws IOException {
        // TODO: Catch Jackson exceptions
        try {
            return this.mapper.writeValueAsString(obj);
        } catch (Exception e) {
            throw e;
        }
        //return null;
    }
}
