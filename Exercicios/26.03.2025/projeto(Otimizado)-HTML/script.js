// Array que armazenará os dados dos usuários carregados do JSON
let usuarios = [];

// Faz a leitura assíncrona do arquivo 'usuarios.json'
fetch('usuarios.json')
    .then(response => response.json()) // Converte a resposta para JSON
    .then(data => {
        // Armazena os dados no array global 'usuarios'
        usuarios = data;

        // Atualiza o status na página
        document.getElementById('status').innerText = "Dados carregados com sucesso!";

        // Habilita todos os botões (que estavam desativados até o carregamento)
        document.querySelectorAll("button").forEach(btn => btn.disabled = false);

        // Exibe os dados carregados no console (útil para debug)
        console.log("Usuários carregados:", usuarios);
    })
    .catch(error => {
        // Em caso de erro no carregamento do JSON
        document.getElementById('status').innerText = "Erro ao carregar os dados.";
        console.error('Erro ao carregar JSON:', error);
    });


// Função para exibir todos os dados dos usuários
function mostrarTodos() {
    const res = usuarios.map(u =>
        `${u.nome}, ${u.idade} anos, ${u.homem ? 'Homem' : 'Mulher'}, ${u.peso}kg, ${u.altura}m`
    ).join('<br>');

    document.getElementById('resultado').innerHTML = res;
}


// Calcula o IMC (Índice de Massa Corporal)
function calcularIMC(peso, altura) {
    return peso / (altura * altura);
}


// Classifica o IMC conforme faixas padrão
function classificarIMC(imc) {
    if (imc <= 18.5) return 'abaixo do peso';
    else if (imc <= 25) return 'peso normal';
    else return 'sobrepeso';
}


// Exibe o IMC e a classificação de todos os usuários
function mostrarIMC() {
    const res = usuarios.map(u => {
        const imc = calcularIMC(u.peso, u.altura);
        return `${u.nome} tem IMC ${imc.toFixed(2)} e está ${classificarIMC(imc)}.`;
    }).join('<br>');

    document.getElementById('resultado').innerHTML = res;
}


// Mostra o IMC e classificação apenas dos homens
function imcHomens() {
    const res = usuarios
        .filter(u => u.homem) // Filtra apenas usuários do sexo masculino
        .map(u => {
            const imc = calcularIMC(u.peso, u.altura);
            return `${u.nome} tem IMC ${imc.toFixed(2)} e está ${classificarIMC(imc)}.`;
        }).join('<br>');

    document.getElementById('resultado').innerHTML = res;
}


// Mostra o IMC e classificação apenas das mulheres
function imcMulheres() {
    const res = usuarios
        .filter(u => !u.homem) // Filtra apenas usuários do sexo feminino
        .map(u => {
            const imc = calcularIMC(u.peso, u.altura);
            return `${u.nome} tem IMC ${imc.toFixed(2)} e está ${classificarIMC(imc)}.`;
        }).join('<br>');

    document.getElementById('resultado').innerHTML = res;
}


// Calcula e mostra a média de IMC dos homens
function mediaIMCHomens() {
    const homens = usuarios.filter(u => u.homem); // Filtra homens

    // Soma dos IMCs dos homens
    const soma = homens.reduce((acc, u) => acc + calcularIMC(u.peso, u.altura), 0);

    const media = soma / homens.length; // Média dos IMCs

    document.getElementById('resultado').innerHTML = `Média de IMC dos homens: ${media.toFixed(2)}`;
}


// Calcula e mostra a média de IMC das mulheres
function mediaIMCMulheres() {
    const mulheres = usuarios.filter(u => !u.homem); // Filtra mulheres

    // Soma dos IMCs das mulheres
    const soma = mulheres.reduce((acc, u) => acc + calcularIMC(u.peso, u.altura), 0);

    const media = soma / mulheres.length; // Média dos IMCs

    document.getElementById('resultado').innerHTML = `Média de IMC das mulheres: ${media.toFixed(2)}`;
}


// Exibe a pessoa mais alta e a mais baixa da lista
function pessoaAltaBaixa() {
    if (usuarios.length === 0) return; // Garante que há usuários

    // Inicializa com o primeiro usuário
    let maisAlto = usuarios[0];
    let maisBaixo = usuarios[0];

    // Percorre todos os usuários comparando alturas
    usuarios.forEach(u => {
        if (u.altura > maisAlto.altura) maisAlto = u;
        if (u.altura < maisBaixo.altura) maisBaixo = u;
    });

    // Exibe os resultados
    document.getElementById('resultado').innerHTML =
        `Pessoa mais alta: ${maisAlto.nome} com ${maisAlto.altura}m<br>` +
        `Pessoa mais baixa: ${maisBaixo.nome} com ${maisBaixo.altura}m`;
}
