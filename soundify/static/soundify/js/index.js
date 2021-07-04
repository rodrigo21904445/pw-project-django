function showPage(section) {
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => document.querySelector('#main-content').innerHTML = text);
}

document.addEventListener('DOMContentLoaded', () => {    

    document.querySelectorAll('nav').forEach(a => {
        a.onclick = () => {
            showPage(this.dataset.section);
        };
    });

    const genresCuriosidades = {
        'rock': 'Rock é um termo abrangente que define um gênero musical de música popular que se desenvolveu durante e após a década de 1950.',
        'metal': 'As primeiras bandas de heavy metal como Led Zeppelin, Deep Purple e Black Sabbath atraíram um grande público, apesar de muitas vezes serem desdenhadas pelos críticos, um fato comum em toda a história do gênero.',
        'blues': 'O gênero se desenvolveu a partir de raízes das tradições musicais africanas, canções de trabalho afro-americanas, spirituals e música tradicional.',
        'hiphop': 'Hip hop é um gênero musical, com uma subcultura própria, iniciado durante a década de 1970, nas comunidades jamaicanas, latinas e afro-americanas da cidade de Nova Iorque. Afrika Bambaataa, reconhecido como o criador do movimento, estabeleceu quatro pilares essenciais na cultura hip hop: o rap, o DJing, breakdance e o graffiti. Outros elementos incluem a moda hip hop e gírias.',
        'rb': 'O termo R&B foi usado originalmente para descrever gravações comercializadas predominantemente por artistas Afro-americanos.',
        'jazz': 'A manifestação de Jazz terá surgido por volta do final do século XIX na região de Nova Orleães, tendo origem na cultura popular e na criatividade das comunidades negras que ali viviam.',
        'pop': 'A música pop é eclética, e muitas vezes incorpora elementos de outros estilos, como o urban, dance, rock, música latina, soul e country.',
        'eletronic': 'A música eletrónica ou eletrônica é toda música que é criada ou modificada através do uso de equipamentos e instrumentos eletrônicos.',
        'latin': 'A musica latina faz parte desde a simples música do norte do México à sofisticada havaneira de Cuba, bem como as sinfonias de Heitor Villa-Lobos e os simples sons da quena.',
    }

    document.getElementById('rock').onclick = () => {
        alert(genresCuriosidades['rock']);
    }

    document.getElementById('metal').onclick = () => {
        alert(genresCuriosidades['metal']);
    }
    
    document.getElementById('blues').onclick = () => {
        alert(genresCuriosidades['blues']);
    }

    document.getElementById('hiphop').onclick = () => {
        alert(genresCuriosidades['hiphop']);
    }

    document.getElementById('rb').onclick = () => {
        alert(genresCuriosidades['rb']);
    }

    document.getElementById('jazz').onclick = () => {
        alert(genresCuriosidades['jazz']);
    }

    document.getElementById('pop').onclick = () => {
        alert(genresCuriosidades['pop']);
    }

    document.getElementById('eletronic').onclick = () => {
        alert(genresCuriosidades['eletronic']);
    }

    document.getElementById('latin').onclick = () => {
        alert(genresCuriosidades['latin']);
    }
});
