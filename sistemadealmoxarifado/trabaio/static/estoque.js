document.addEventListener('DOMContentLoaded', () => {
  const botao = document.getElementById('botaofiltro');
  const conteudo = document.getElementById('conteudo-container');

  // Garante que o botão e o conteúdo realmente existem na página
  if (botao && conteudo) {
    botao.addEventListener('click', (event) => {
     
      // Mostra/Esconde o conteúdo
      conteudo.classList.toggle('escondido');
    });
  } else {
    console.error("Não encontrei o botão ou o conteúdo! Verifique os IDs.");
  }
});

botao.addEventListener('click', () => {
  conteudo.classList.toggle('escondido');
});
