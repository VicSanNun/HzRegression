### Explorando Machine Learning na reconstrução da taxa de expansão do Universo, $H(z)$.

O objetivo deste trabalho é estudar diferentes abordagens na reconstrução de $H(z)$, utilizando dados de cronômetros cósmicos, por meio de Processos Gaussianos e MCMC (Monte Carlo-Markov Chain).

#### Um pouco de Cosmologia
As 3 equações que governam a dinâmica cósmica são chamadas de **Equações de Friedmann**. Neste trabalho, focaremos nossos esforços somente na 1ª Equação,
$$
H_{t}^{2} = \frac{8}{3} \pi G \rho_{t} - \frac{K}{a_{t}^{2}}.
$$
Essa expressão relaciona a expansão do universo com a energia responsável por essa expansão/contração.

Realizando uma mudança de variável $t \to z$ ($z$ é o [*redshift*](https://pt.wikipedia.org/wiki/Desvio_para_o_vermelho)), e aplicando as premissas do modelo cosmológico padrão, $\Lambda CDM$, podemos reescrever a equação como
$$
H(z) = H_{0} \sqrt{\Omega_{m}(1+z)^{3}+(1-\Omega_{m})}.
$$

Observações da matéria e da energia escura, nos levam a valores médios aproximados da constante de Hubble,  $H_{0} = 70 \ km \cdot s^{-1} \cdot Mpc^{-1}$, e da densidade de matéria do universo, $\Omega_{m} = 0.3$ (sim, é adimensional). Dessa forma,

$$
H_{\Lambda CDM} = 70 \sqrt{0.3(1+z)^{3}+0.7)}.
$$

Você pode estar se perguntando: **se já sabemos a expressão que modela $H(z)$, pra que reconstuir?** Bom, te respondo com outra pergunta: e se o modelo teórico-observacional estiver errado? A vantagem de reconstruir com métodos não paramétricos, é que essa abordagem é bem flexível e se adapta muito bem aos dados. Além disso, ela não precisa pressupor uma relação entre os dados. Em adição, ao utilizar dados de cronômetros cósmicos, que são ṕuramente observacionais e independente de modelo, conseguimos gerar uma reconstrução *fair*. Porém, como veremos adiante, o Processo Gaussiano aceita que eu passe $H_{\Lambda CDM}$ como um *ansatz* para função média que descreva os dados, $\mu$. Um dos nossos objetivos é explorar a diferença no resultado ao considerar $\mu = 0$ e $\mu = H_{\Lambda CDM}$.


#### Processos Gaussianos
Um Processo Gaussiano **é uma ferramenta de machine learning utilizada para reconstruir, de maneira não paramétrica, uma função que descreva um conjunto de dados**. De maneira um pouco mais aprofundada, esse instrumento utiliza **inferência Bayesiana para construir uma distribuição multivariada no espaço de funções**.

Para realizar a regressão (ou reconstrução), o processo necessita de algumas coisas:
* Dados de entrada, $(X, Y)$;
* Um _ansatz_ para função média que descreva os dados, $\mu (x)$;
* Uma função de covariância, também chamada de kernel, $k(x, \bar{x})$.

A função $k(x, \bar{x})$ depende, por sua vez, de alguns hiperparâmetros que variam dependendo da escolha da função. Neste trabalho, vamos utilizar a função _squared exponential_:

$$
k(x, \bar{x}) = \sigma^{2}_{f}\exp \Bigg( - \frac{(x-\bar{x})^{2}}{2l^{2}}\Bigg).
$$

Essa função depende dos hiperparâmetros $\sigma$ e $l$.

Dessa forma, podemos descrever nossos dados como:

$$
f(x) \sim \mathcal{GP}(\mu(x), \ k(x, \ \bar{x})).
$$

#### O Problema
Esse procedimento vem sido utilizado durante décadas para reconstrução de diferentes observáveis cosmológicos. Porém, até o momento, poucos pesquisadores exploraram o impacto da seleção da função média, $\mu(x)$, e da escolha dos hiperparâmetros de $k$, no resultado final da regressão. 

Acontece que $\mu(x)$, como veremos adiante, influencia o resultado do processo. Uma escolha errada desse parâmetro pode induzir um viés na reconstrução. Além disso, uma má seleção de hiperparâmetros para $k(x, \bar{x})$ pode resultar em uma função de covariância imprópria. 

**Em uma abordagem totalmente Bayesiana, os hiperparêmtros de $k(x, \bar{x})$ são obtidos através de uma *marginalização* ao explorar a função de verossimilhança (likelihood).** Porém, em alguns casos, podemos maximizar essa função ao invés de explorá-la. Para marginalizar, utilizamos um algoritmo de **Monte Carlo-Markov Chain** (MCMC).

#### Nossa metodologia

Então faremos 5 reconstruções, com abordagens diferentes para $\mu$, $\sigma$ e $l$, para entender como esses parâmetros influenciam o resultado final da regressão. Para isso, reconstruiremos a taxa de expansão do universo, $H(z)$, utilizando dados de *cronômetros cósmicos*. Em algumas dessas reconstruções utilizaremos $\mu = 0$ e em outras utilizaremos $\mu = H_{\Lambda CDM}$ (modelo cosmológico padrão).
Além disso, em algumas abordagens **maximizaremos** a função de verossimilhança, para obter $\sigma$ e $l$, e em outras, **marginalizaremos** esses hiperparâmetros. Em resumo:

1. Reconstruiremos $H(z)$ utilizando $\mu = 0$ e **maximizando** os hiperparêmtros;
2. reconstruiremos $H(z)$ utilizando $\mu = H_{\Lambda CDM}$ e **maximizando** os hiperparêmtros;
3. reconstruiremos $H(z)$ utilizando $\mu = 0$ e **marginalizando** os hiperparêmtros;
4. reconstruiremos $H(z)$ utilizando $\mu = H_{\Lambda CDM}$ e **marginalizando** os hiperparêmtros;
5. reconstruiremos $H(z)$ utilizando $\mu = H_{\Lambda CDM}$ e **marginalizando** os hiperparêmtros e os parâmetros cosmológicos.

#### Referências

As principais referências deste trabalho são:

1. [Hwang, 2023] S. Hwang, B. L’Huillier, R. E Keeley, Jee. M. J., and A. Shafieloo. **How to use gp: Effects of the mean function and hyperparameter selection on gaussian process regression.**
Journal of Cosmology and Astroparticle Physics, page 14, 2023.

2. [Gonzalez, 2018] Gonzalez. **Reconstrução Não Paramétrica das Perturbações Cosmologicas.** PhD thesis, Observatório Nacional, Rio de Janeiro, Brasil, 2018.

3. [Seikel, 2012] M. Seikel, C. Clarkson, and M. Smith. **Reconstruction of dark energy and expansion dynamics using gaussian processes.** Journal of Cosmology and Astroparticle Physics,
6:36–47, 2012.

4. [Gilks, 1996] W. R. Gilks, S. Richardson, and D. J. Spiegelhalter. **Markov Chain Monte Carlo in Practice.** Springer, 1 edition, 1996.
