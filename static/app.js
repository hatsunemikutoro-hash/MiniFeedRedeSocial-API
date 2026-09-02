

async function createPost(title, body, userid) {
    const container = document.createElement("div");
    const card = document.getElementById("card");
    if (card) {
        card.appendChild(container);
        container.classList.add("box");

        const h3 = document.createElement("h3")
        const p = document.createElement("p");
        container.appendChild(h3);
        container.appendChild(p);

        h3.innerText = title;
        p.innerText = body;
    } else {
        console.log("nao achei?")
    }

}

async function fetchData() {
    try {
        const resposta = await fetch('/import');

        if (!resposta.ok) {
            const erroData = await resposta.json();
            console.error('socorro erro retornado pelo servidor (Flask):', erroData);
            return;
        }
        const posts = await resposta.json();    

        if (Array.isArray(posts)) {
            posts.forEach(element => {
                createPost(element.title, element.body, element.id)
            });
        }
    } catch (error) {
        console.error('erro no fetch', error);
    }
}

fetchData()