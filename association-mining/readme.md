
## Confidence
 * Let X and Y be two sets of items. The confidence
   conf(X ∪ Y ) of the rule X ∪ Y is the conditional probability of X ∪ Y occurring in a
   transaction, given that the transaction contains X. Therefore, the confidence conf(X ⇒ Y )
   is defined as follows:
 * conf(X ⇒ Y ) = sup(X ∪ Y ) / sup(X)
 
## Confidence monotonicity
 * Let X1, X2, and I be itemsets such that X1 ⊂ X2 ⊂ I. Then the confidence of X2 ⇒ I − X2 is at least that of X1 ⇒ I − X1.
 * conf(X2 ⇒ I − X2) ≥ conf(X1 ⇒ I − X1)
 
## Algorithms
 * Apriori
   - This algorithm uses effective prunning of search space with the use of downward closure property.
   - Downward closure property means that subset of large itemset exceeds the minimum required support.
