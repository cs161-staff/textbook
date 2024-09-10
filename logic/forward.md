---
title: "11.6 Forward Chaining"
parent: 11. Logic
nav_order: 6
layout: page
---

# 11.6 Forward Chaining

An algorithm, **forward chaining**, iterates through every implication statement in which the premise (left-hand side) is known to be true, adding the conclusion (right-hand side) to the list of known facts.


## 11.6.1 Forward Chaining: Example

Suppose we had the following knowledge base:
1. $$A \to B$$
2. $$A \to C$$
3. $$B \land C \to D$$
4. $$D \land E \to Q$$
5. $$A \land D \to Q$$
6. $$A$$

We'd like to use forward chaining to determine if $$Q$$ is true or false.


To initialize the algorithm, we'll initialize a list of numbers \textit{count}. The $$i$$th number in the list tells us how many symbols are in the premise of the $$i$$th clause. For example, the third clause $$B \land C \to D$$ has 2 symbols ($$B$$ and $$C$$) in its premise, so the third number in our list should be 2. Note that the sixth clause $$A$$ has 0 symbols in its premise, because it is equivalent to $$\text{True} \to A$$.

Then, we'll initialize \textit{inferred}, a mapping of each symbol to true/false. This tells us which symbols we've found to be true. Initially, all symbols will be false, because we haven't proven any symbols to be true yet.

Finally, we'll initialize a list of symbols \textit{agenda}, which is a list of symbols that we can prove to be true, but have not propagated the effects of yet. For example, if $$D$$ were in the agenda, this would indicate that we're ready to prove that $$D$$ is true, but we still need to check how that affects any of the other clauses. Initially, \textit{agenda} will only contain the symbols we directly know to be true, which is just $$A$$ here. (In other words, \textit{agenda} starts with any clauses with 0 symbols in its premise.)

Our starting state looks like this:
- **count**:$$[1, 1, 2, 2, 2, 0]$$
- **inferred**: $$\{A:F, B:F, C:F, D:F, E:F, Q:F\}$$
- **agenda**: $$[A]$$


On each iteration, we'll pop an element off \textit{agenda}. Here, there's only one element that we can pop off: $$A$$. The symbol we popped off is not the symbol we want to analyze ($$Q$$), so we're not done with the algorithm yet.

According to the \textit{inferred} table, $$A$$ is false. However, since we've just popped $$A$$ off the agenda, we're able to set it to true.

Next, we need to propagate the consequences of $$A$$ being true. For each clause where $$A$$ is in the premise, we'll decrement its corresponding count to indicate that there is one fewer symbol in the premise that needs to be checked. In this example, clauses 1, 2, and 5 contain $$A$$ in the premise, so we'll decrement elements 1, 2, and 5 in \textit{count}.

Finally, we check if any clauses have reached a count of 0. We note that this happened on clauses 1 and 2. This indicates that every premise in clauses 1 and 2 have been satisfied, so the conclusions in clauses 1 and 2 are ready to be inferred. For example, in clause 1, all premises (just $$A$$ here) have been satisfied, so the conclusion $$B$$ is ready to be inferred. We'll add the conclusions in clauses 1 and 2 to the agenda.

After iteration 0, our algorithm look like this:
- **count**:$$[{\color{red} 0}, {\color{red} 0}, 2, 2, {\color{red} 1}, 0]$$
- **inferred**: $$\{A:T, B:F, C:F, D:F, E:F, Q:F\}$$
- **agenda**: $$[{\color{red} B}, {\color{red} C}]$$


On the next iteration, we'll pop an element off \textit{agenda}. Here we've chosen to pop off $$B$$. The symbol we popped off is not the symbol we want to analyze ($$Q$$), so we're not done with the algorithm yet.

According to the \textit{inferred} table, $$B$$ is false. However, since we've just popped $$B$$ off the agenda, we're able to set it to true.

Next, we need to propagate the consequences of $$B$$ being true. The only clause where $$B$$ is in the premise is clause 3. We have to decrement its corresponding count.

Finally, we check if any clauses have reached a count of 0. None of the clauses have newly reached a count of 0, so we can't draw any new conclusions, and we can't add anything new to the agenda.

After iteration 1, our algorithm look like this:
- **count**:$$[0, 0, {\color{red} 1}, 2, 1, 0]$$
- **inferred**: $$\{A:T, {\color{red} B:T}, C:F, D:F, E:F, Q:F\}$$
- **agenda**: $$[C]$$


Next, we'll pop off $$C$$ from the \textit{agenda} (which is not $$Q$$ so the algorithm isn't done yet). We can set $$C$$ to true on the \textit{inferred} list.

To propagate the consequences of $$C$$ being true, we decrement the count for clause 3 (the only clause with $$C$$ in the premise).

Clause 3 has newly reached a count of 0, so we can add its conclusion, $$D$$, to the agenda.

After iteration 2, our algorithm look like this:
- **count**:$$[0, 0, {\color{red} 0}, 2, 1, 0]$$
- **inferred**: $$\{A:T, B:T, {\color{red} C:T}, D:F, E:F, Q:F\}$$
- **agenda**: $$[{\color{red} D}]$$


Next, we'll pop off $$D$$ from the \textit{agenda} (not $$Q$$, so algorithm isn't done). We can set $$D$$ to true on the \textit{inferred} list.

To propagate the consequences of $$D$$ being true, we decrement the counts for clauses 4 and 5 (which contain $$D$$ in the premise).

Clause 5 has newly reached a count of 0, so we add its conclusion, $$Q$$, to the agenda.

After iteration 3, our algorithm look like this:
- **count**:$$[0, 0, 0, {\color{red} 1}, {\color{red} 0}, 0]$$
- **inferred**: $$\{A:T, B:T, C:T, {\color{red} D:T}, E:F, Q:F\}$$
- **agenda**: $$[{\color{red} Q}]$$


Next, we'll pop off $$Q$$ from the \textit{agenda}. This is the symbol we wanted to evaluate, and popping it off the agenda indicates that it has been proven to be true. We conclude that $$Q$$ is true and finish the algorithm.