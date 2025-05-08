NAME:- SACHIN RAJESH PAL
REG NO.:- RA2211027010061
Real-Time QoS Optimization for Game Streaming Platforms 

With the rise of live game streaming platforms like Twitch and YouTube Gaming, it's becoming harder to keep stream quality consistent. Network conditions change, viewer engagement fluctuates, and streams can vary in quality. Traditional methods of managing QoS (Quality of Service) often don't react fast enough to these dynamic situations.

This project is a smarter, data-driven approach to real-time QoS optimization. It combines:

* A deep learning model that predicts how satisfied users are based on network data.
* BERT, a language model that analyzes what viewers are saying in chat to detect positive or negative sentiment.
* A system that brings it all together to adjust QoS parameters like bandwidth and latency on the fly.


How It Works 

1. Preprocess QoS Data
   We take in data like latency, bitrate, and packet loss, and scale it so it can be used by our model.

2. Predict User Satisfaction (DNN Classifier)
   A neural network classifies whether the current QoS is likely to leave viewers satisfied or not.

3. Understand Viewer Sentiment (BERT)
   Live chat messages are analyzed using BERT to detect if viewers are happy or frustrated.

4. Adapt in Real Time
   If the system detects issues—either from poor metrics or unhappy chat messages—it suggests actions like increasing bandwidth or reducing latency.


 Example Input

```python
qos_data = pd.DataFrame({
    'latency': [20, 30, 25, 40],
    'bitrate': [5000, 4500, 5200, 4800],
    'packet_loss': [0.1, 0.05, 0.07, 0.02]
})

chat_data = [
    "This stream is amazing!",
    "Why is it lagging so much?",
    "The quality is really good today.",
    "Buffering again... not great."
]
```



Getting Started 

1. Clone the repository:

```bash
git clone https://github.com/your-username/real-time-qos-optimization.git
cd real-time-qos-optimization
```

2. Install required packages:

```bash
pip install torch transformers pandas scikit-learn
```

3. Run the script:

```bash
python Real_Time_QoS_Optimization.py
```

---

 What It Can Be Used For

* Keeping stream quality high even when networks are unstable.
* Detecting viewer frustration early and reacting in real-time.
* Enhancing the streaming experience for both streamers and viewers.



 What’s Next?

* Connect to live Twitch/YouTube APIs for real-time data
* Train BERT on actual chat data from game streams
* Add more QoS actions like dynamic resolution switching






