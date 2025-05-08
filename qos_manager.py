import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import logging

class QoSManager:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.sentiment_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
        self.scaler = StandardScaler()
        self.logger = logging.getLogger(__name__)
        
    def analyze_stream_metrics(self, metrics):
        """
        Analyze real-time streaming metrics
        metrics: dict containing bitrate, latency, packet_loss, etc.
        """
        try:
            # Normalize metrics
            normalized_metrics = self.scaler.fit_transform(
                np.array([[
                    metrics['bitrate'],
                    metrics['latency'],
                    metrics['packet_loss'],
                    metrics['buffer_size']
                ]])
            )
            
            # Calculate QoS score (0-100)
            qos_score = self._calculate_qos_score(normalized_metrics[0])
            return qos_score
        except Exception as e:
            self.logger.error(f"Error analyzing stream metrics: {str(e)}")
            return None

    def analyze_sentiment(self, chat_messages):
        """
        Analyze viewer sentiment from chat messages
        chat_messages: list of chat messages
        """
        try:
            sentiments = []
            for message in chat_messages:
                inputs = self.tokenizer(message, return_tensors="pt", truncation=True, padding=True)
                outputs = self.sentiment_model(**inputs)
                sentiment = outputs.logits.argmax().item()
                sentiments.append(sentiment)
            
            # Calculate average sentiment
            avg_sentiment = np.mean(sentiments)
            return avg_sentiment
        except Exception as e:
            self.logger.error(f"Error analyzing sentiment: {str(e)}")
            return None

    def _calculate_qos_score(self, normalized_metrics):
        """
        Calculate QoS score based on normalized metrics
        """
        weights = {
            'bitrate': 0.3,
            'latency': 0.3,
            'packet_loss': 0.2,
            'buffer_size': 0.2
        }
        
        score = (
            normalized_metrics[0] * weights['bitrate'] +
            (1 - normalized_metrics[1]) * weights['latency'] +
            (1 - normalized_metrics[2]) * weights['packet_loss'] +
            normalized_metrics[3] * weights['buffer_size']
        ) * 100
        
        return max(0, min(100, score))

    def optimize_stream_parameters(self, qos_score, sentiment_score, current_params):
        """
        Optimize streaming parameters based on QoS and sentiment scores
        """
        try:
            # Define parameter adjustment ranges
            bitrate_adjustment = 0.1
            buffer_adjustment = 0.05
            
            # Adjust parameters based on scores
            if qos_score < 70:
                current_params['bitrate'] *= (1 - bitrate_adjustment)
                current_params['buffer_size'] *= (1 + buffer_adjustment)
            elif qos_score > 90 and sentiment_score > 0.7:
                current_params['bitrate'] *= (1 + bitrate_adjustment)
                current_params['buffer_size'] *= (1 - buffer_adjustment)
            
            return current_params
        except Exception as e:
            self.logger.error(f"Error optimizing stream parameters: {str(e)}")
            return current_params 