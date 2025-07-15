package com.web;
// config/WebSocketConfig.java


import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.web.socket.config.annotation.*;


@Configuration
@EnableWebSocketMessageBroker
@EnableWebSocket
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws") // WebSocket endpoint
                .setAllowedOrigins("http://localhost:3001") // Allow React origin
                .withSockJS(); // Use SockJS fallback

    }

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic"); // For subscriptions
        config.setApplicationDestinationPrefixes("/app"); // For sending messages
    }
}


/*
@Configuration
@EnableWebSocket


public class WebSocketConfig implements WebSocketConfigurer {

    private final MyWebSocketHandler webSocketHandler;

    public WebSocketConfig(MyWebSocketHandler webSocketHandler) {
        this.webSocketHandler = webSocketHandler;
    }

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(new MyWebSocketHandler(), "/ws/chat").setAllowedOrigins("*");
    }
}
*/
