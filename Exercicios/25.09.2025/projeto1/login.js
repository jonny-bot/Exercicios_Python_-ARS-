function fazerLogin() {
  const usuarioInput = document.getElementById('usuario').value;
  const senhaInput = document.getElementById('senha').value;
  const mensagemErro = document.getElementById('mensagemErro');

  const funcionario = funcionarios.find(f =>
    f.usuario === usuarioInput && f.senha === senhaInput
  );

  if (funcionario) {
    // Salva info no localStorage para usar no PDV
    localStorage.setItem('funcionarioLogado', JSON.stringify(funcionario));
    window.location.href = 'pdv.html'; // redireciona para o PDV
    return false;
  } else {
    mensagemErro.textContent = 'Usuário ou senha inválidos.';
    return false; // evita recarregar a página
  }
}
