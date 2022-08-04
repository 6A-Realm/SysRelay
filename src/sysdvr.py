import cv2
from rich.console import Console

console = Console()

class SwitchStream():
    def __init__(self, SwitchIP):
        self.ip = SwitchIP
        self.stream = None

    def showStream(self):
        console.print(f"Streaming from {self.ip}.", style = "green")
        self.stream = cv2.VideoCapture(f"rtsp://root:pass@{self.ip}:6666//rtplive/_definst_/hessdalen03.stream")
        while(self.stream.isOpened()):
            ret, frame = self.stream.read()
            cv2.imshow(f"RSTP: {self.ip}", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        self.stream.release()
        cv2.destroyAllWindows()