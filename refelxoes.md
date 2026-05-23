## Aula 06 — Verificação de LSP

Ao revisar as subclasses Notebook, Projetor e Cabo, foi verificado que todas respeitam o contrato definido pela classe base Equipamento.

calcular_multa(0) retorna 0.0 em todas as subclasses.

calcular_multa(-5) também retorna 0.0, evitando valores negativos.

Nenhuma das subclasses lança exceções inesperadas.

O contrato da classe base define retorno do tipo float maior ou igual a zero, sem exceções. Todas as subclasses respeitam esse comportamento, portanto o princípio LSP está satisfeito.

Isso significa que qualquer subclasse pode substituir Equipamento sem quebrar o funcionamento do ServicoEmprestimo.


## Aula 06 — DIP

A aplicação do DIP mudou a relação de dependência entre os módulos. Antes, o ServicoEmprestimo criava internamente o repositório e o notificador, ficando diretamente acoplado às implementações concretas. Depois da alteração, ele passou a receber essas dependências pelo construtor.

Essa mudança não foi apenas técnica, mas também conceitual. O serviço deixou de controlar quais implementações utilizar e passou a depender apenas das abstrações necessárias para funcionar. Isso reduz o acoplamento e facilita a substituição das dependências por implementações falsas durante testes.

Segundo Valente, no Capítulo 5 de Engenharia de Software Moderna, “módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações”. A aplicação do DIP no projeto demonstra exatamente essa ideia, tornando o sistema mais flexível, desacoplado e testável.