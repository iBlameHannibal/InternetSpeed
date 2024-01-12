import speedtest
import pyfiglet

# - - - - -- -   - - - -- -  - --  - - - - - - -  -

Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z = '\033[2;31m'  # Red, second shade
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\033[2;36m'  # Cyan
Y = '\033[1;34m'  # Light blue

logo = pyfiglet.figlet_format('Internet Test')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def internet_speed_test():
    st = speedtest.Speedtest()
    
    
    st.get_best_server()

    
    download_speed = st.download() / 1_000_000

    
    upload_speed = st.upload() / 1_000_000

    
    ping = st.results.ping

    print(Y + logo)

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    internet_speed_test()
