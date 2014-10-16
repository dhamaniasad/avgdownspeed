import requests
import time


def download_file(url):
    filename = url.split('/')[-1]
    with open('/tmp/' + filename, 'wb') as f:
        start = time.time()
        r = requests.get(url, stream=True)
        total_length = r.headers['content-length']
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        stop = time.time()
        time_taken = stop - start
        download_speed = int(total_length) / int(time_taken)
        download_speed = download_speed / 1024
        if download_speed >= 1024:
            download_speed = download_speed / 1024
            MB = "MB(megabytes) per second"
            print "Average download speed: %s %s" % (download_speed, MB)
        elif download_speed < 1024:
            KB = "KB(kilobytes) per second"
            print "Average download speed: %s %s" % (download_speed, KB)


def main():
    url = "http://cachefly.cachefly.net/10mb.test"
    download_file(url)


if __name__ == "__main__":
    main()
