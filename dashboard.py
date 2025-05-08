import streamlit as st
import plotly.graph_objects as go
import time
import numpy as np

class StreamDashboard:
    def __init__(self, qos_manager, stream_monitor):
        self.qos_manager = qos_manager
        self.stream_monitor = stream_monitor
        self.metrics_history = []
        self.sentiment_history = []
        
    def run(self):
        st.title("Live Stream QoS Dashboard")
        
        # Start monitoring
        self.stream_monitor.start_monitoring()
        
        # Create placeholder for metrics
        metrics_placeholder = st.empty()
        sentiment_placeholder = st.empty()
        
        while True:
            # Update metrics
            metrics = self.stream_monitor._collect_metrics()
            chat_messages = self.stream_monitor._collect_chat_messages()
            
            qos_score = self.qos_manager.analyze_stream_metrics(metrics)
            sentiment_score = self.qos_manager.analyze_sentiment(chat_messages)
            
            # Update history
            self.metrics_history.append(qos_score)
            self.sentiment_history.append(sentiment_score)
            
            # Create metrics chart
            fig_metrics = go.Figure()
            fig_metrics.add_trace(go.Scatter(
                y=self.metrics_history[-100:],
                name="QoS Score"
            ))
            fig_metrics.update_layout(title="QoS Score Over Time")
            
            # Create sentiment chart
            fig_sentiment = go.Figure()
            fig_sentiment.add_trace(go.Scatter(
                y=self.sentiment_history[-100:],
                name="Sentiment Score"
            ))
            fig_sentiment.update_layout(title="Sentiment Score Over Time")
            
            # Update placeholders
            metrics_placeholder.plotly_chart(fig_metrics)
            sentiment_placeholder.plotly_chart(fig_sentiment)
            
            time.sleep(1)

if __name__ == "__main__":
    # Initialize components
    qos_manager = QoSManager()
    stream_monitor = StreamMonitor(qos_manager)
    dashboard = StreamDashboard(qos_manager, stream_monitor)
    
    # Run dashboard
    dashboard.run() 