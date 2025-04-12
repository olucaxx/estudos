{
  a <- 90 # primero valor
  b <- 54 # segundo valor

  getNextPrimeNum <- function(currentNum) {
    newNum <- currentNum + 1
    repeat {
      # verifica se é primo
      for (i in 3:newNum-1) { 
      # elimina o 0, o 1 e o próprio número, se qualquer um entre esses dividir, não é primo
        if (newNum %% i == 0) {
          newNum <- newNum + 1
          next # esse next vai no repeat, reseta o loop for
        }
      }
      return (newNum) # quando achar o primo, retorna ele, quebrando o repeat
    }
  }
  
  getMDC <- function(n1, n2) {
    mdc <- 1 # valor do mdc
    i <- 2 # número primo inicial
    while (i <= n1 | i <= n2){ 
    # o número primo não pode ser maior que nenhum dos dois, se não é impossivel dividir
      if (n1 %% i == 0 & n2 %% i == 0) { 
      # tem que conseguir dividir os dois ao mesmo tempo
        n1 <- n1 %/% i
        n2 <- n2 %/% i
        mdc <- mdc * i
      } else {
      # se não divide os dois, tenta o próximo número primo, até quebrar o while em algum momento
        i <- getNextPrimeNum(i)
      }
    }
    return(mdc)
  }
  
  getMMC <- function(n1, n2) {
    mmc <- 1 # valor do mmc
    i <- 2 # número primo inicial
    while (n1 != 1 | n2 != 1) { 
    # os dois precisam ser igual a 1 para finalizar o mmc
      if (n1 %% i != 0 & n2 %% i != 0) {
      # não divide nenhum dos dois, então precisamos do próximo número primo
        i <- getNextPrimeNum(i)
      }
      # se der pra dividir os dois juntos, pula os if's abaixo com o next (igual o continue)
      if (n1 %% i == 0 & n2 %% i == 0) {
        n1 <- n1 %/% i
        n2 <- n2 %/% i
        mmc <- mmc * i
        next
      }
      # tenta dividir o primeiro número
      if (n1 %% i == 0) {
        n1 <- n1 %/% i
        mmc <- mmc * i
      }
      # tenta dividir o segundo número
      if (n2 %% i == 0) {
        n2 <- n2 %/% i
        mmc <- mmc * i
      }
    }
    return(mmc)
  }

  print(getMMC(a,b))
  print(getMDC(a,b))
}
