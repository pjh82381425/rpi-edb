function updateTime() {
    fetch('/get_time')
        .then(response => response.json())
        .then(data => {
            // ✅ 현재 시간 업데이트
            const current_time = `${data.ampm} ${data.hour}:${data.minute}`;
            const second = `${data.second}`;
            document.getElementById('current-time').textContent = current_time;
            document.getElementById('second').textContent = second;
        })
        .catch(error => {
            console.error('데이터를 가져오는 데 오류가 발생했습니다:', error);
        });
}

function updateIcon() {
    fetch('/get_hour_24')
        .then(response => response.json())
        .then(data => {
            // ✅ 시간 아이콘 업데이트
            let hour_24 = ~~data.hour_24; // 받은 데이터에서 24시간제 시간변수를 정수로 저장
            if (6 < hour_24 && hour_24 < 12) {
                document.getElementById("a").style.display = "block";
                document.getElementById("b").style.display = "none";
                document.getElementById("c").style.display = "none";
            } else if (12 <= hour_24 && hour_24 <= 18) {
                document.getElementById("a").style.display = "none";
                document.getElementById("b").style.display = "block";
                document.getElementById("c").style.display = "none";
            } else {
                document.getElementById("a").style.display = "none";
                document.getElementById("b").style.display = "none";
                document.getElementById("c").style.display = "block";
            }
        })
        .catch(error => {
            console.error('데이터를 가져오는 데 오류가 발생했습니다:', error);
        });
}

function updateEnvironment() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            // ✅ 온도 업데이트
            const temperature = data.temperature ?? 'N/A';
            document.getElementById('temperature').textContent = `${temperature}`;
            const tempBox = document.getElementById('temperature-box');

            let alpha = 0.3;  // 투명도 고정

            if (temperature !== 'N/A') {
                let red = 100, green = 255, blue = 150;

                let redIntensity = Math.min(1, (temperature - 25) / 15); // 40°C에서 빨강 증가
                let blueIntensity = Math.min(1, (25 - temperature) / 25); // 0°C에서 파랑 증가

                red = Math.round(100 + redIntensity * (255 - 100));
                blue = Math.round(150 + blueIntensity * (255 - 150));

                let greenReduction = Math.max(redIntensity, blueIntensity);
                green = Math.round(255 - greenReduction * (255 - 100));

                tempBox.style.backgroundColor = `rgba(${red}, ${green}, ${blue}, ${alpha})`;
            }

            // ✅ 습도 업데이트
            const humidity = data.humidity ?? 'N/A';
            document.getElementById('humidity').textContent = `${humidity}`;
            const humidityBox = document.getElementById('humidity-box');

            if (humidity !== 'N/A') {
                let hum_alpha = (humidity / 100) * 0.3;
                humidityBox.style.backgroundColor = `rgba(100, 150, 255, ${hum_alpha})`;
            }

            // ✅ 미세먼지 업데이트
            const pm25 = data.pm25 ?? 'N/A';
            document.getElementById('pm25').textContent = `${pm25}`;
            const pm25Box = document.getElementById('pm25-box');

            if (pm25 !== 'N/A') {
                let pm25_alpha = (pm25 / 100) * 0.3;
                pm25Box.style.backgroundColor = `rgba(100, 150, 255, ${pm25_alpha})`;
            }
        })
        .catch(error => {
            console.error('데이터를 가져오는 데 오류가 발생했습니다:', error);
        });
}

function updateVer() {
    fetch('/get_ver')
        .then(response => response.json())
        .then(data => {
            const ver = data.ver ?? 'N/A';
            document.getElementById('ver').textContent = `${ver}`;
        })
        .catch(error => {
            console.error('데이터를 가져오는 데 오류가 발생했습니다:', error);
        });
}

// ✅ 초기 데이터 업데이트 및 각기 다른 간격으로 갱신
updateTime();
updateEnvironment();
updateIcon();
updateVer();
setInterval(updateTime, 1000); // 1초마다 시간 업데이트
setInterval(updateEnvironment, 2500); // 2.5초마다 환경 데이터 업데이트
setInterval(updateIcon, 60250); // 1분 + 0.25초 마다 아이콘 업데이트
