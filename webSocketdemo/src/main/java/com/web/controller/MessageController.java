package com.web.controller;

import com.web.MyWebSocketHandler;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.Map;

@RestController("/api/chat")
@CrossOrigin(origins = "http://localhost:3001")
public class MessageController {

    @GetMapping("/")
    public String replyToClient(){
        return "Hello there";
    }
    private final MyWebSocketHandler webSocketHandler;

    public MessageController(MyWebSocketHandler webSocketHandler) {
        this.webSocketHandler = webSocketHandler;
    }

    @PostMapping("/send")
    public ResponseEntity<String> sendMessage(@RequestBody Map<String, String> payload) throws IOException {
        String message = payload.get("message");
        webSocketHandler.sendMessageToAll(message);
        return ResponseEntity.ok("Message sent to WebSocket clients")   ;
    }

}
