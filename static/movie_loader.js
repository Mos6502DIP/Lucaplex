function getQueryParameter(name) {
            const urlParams = new URLSearchParams(window.location.search);
            return urlParams.get(name);
        }

        function loadVideo() {
            const movieName = getQueryParameter('movie_name');
            if (movieName) {
                const iframe = document.getElementById('videoIframe');
                iframe.src = `/video_load/${encodeURIComponent(movieName)}`;
            }
        }

        // Load the video when the page loads
        window.onload = loadVideo;