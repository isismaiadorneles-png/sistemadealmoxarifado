//abaixo é uma função para que ao clicar em um botao ele fique de uma cor e os outros voltem para cor origem
const botoes = document.querySelectorAll(".btn-setor");
botoes.forEach(botao => {
  botao.addEventListener("click", () => {
    botoes.forEach(btn => {
      btn.classList.remove("ativo");
    });
    botao.classList.add("ativo");  
  });
});

//abaixo é uma função para filtrar os itens da categoria selecionada
function filtrar(categoria){
  let produtos = document.getElementsByClassName("produto"); //aqui ele pega todos os elementos que têm a classe produto
  for (var i =0; i < produtos.length; i++){//aqui o java começa do primeiro produto e passa por todos eles 
      if (categoria === "Todos") {
      produtos[i].style.display = "table-row"; //se clicar na categoria todos entao vai aparecer a linha de tabela, ou seja nao sera por uma classe especifica mas sim pela TR que é linha da table
    }
   else if (produtos[i].classList.contains(categoria)){
   produtos[i].style.display = "table-row"; //aqui tambem tem table row mas diferencia pq aqui ele pede pra mostrar uma TR com uma classe especifica desejaada 
  }
   else{
    produtos[i].style.display = "none"; //aqui diz que caso nao tem a classe desejada entao desaparece
     }}
}