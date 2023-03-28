from pytube import YouTube
progress_func = ()
complete_func = ()
my_proxies = ()
yt = YouTube(
    'https://www.youtube.com/watch?v=kqtD5dpn9C8&t=263s',
    on_progress_callback = progress_func,
    on_complete_callback = complete_func,
    proxies = my_proxies,
    use_oauth = False,
    allow_oauth_cache=True
    )

print(yt.streams.filter(file_extension='mp4'))
stream = yt.streams.get_by_itag(22)
stream.download()
