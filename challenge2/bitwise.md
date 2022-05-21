===UND===
[[File:0...15 AND.svg|thumb|Bitwise AND of [[4-bit computing|4-bit]] integers]]
Ein '''bitweises UND''' ist eine [[binäre Operation]], die zwei binäre Darstellungen gleicher Länge nimmt und die [[logische Verknüpfung|logisches UND]]-Operation an jedem Paar der entsprechenden Bits durchführt. Wenn also beide Bits in der verglichenen Position 1 sind, ist das Bit in der resultierenden binären Darstellung 1 (1&nbsp;× 1&nbsp;= 1); andernfalls ist das Ergebnis 0 (1&nbsp;× 0&nbsp;= 0 und 0&nbsp;× 0&nbsp;= 0). Zum Beispiel:

     010'''1''' (dezimal 5)
 AND 001'''1''' (Dezimal 3)
   = 000'''1''' (dezimal 1)

Die Operation kann verwendet werden, um zu bestimmen, ob ein bestimmtes Bit „gesetzt“ (1) oder „frei“ (0) ist. Zum Beispiel verwenden wir bei einem Bitmuster 0011 (dezimal 3) ein bitweises UND mit einem Bitmuster, das nur im zweiten Bit eine 1 enthält, um festzustellen, ob das zweite Bit gesetzt ist:

     00'''1'''1 (Dezimal 3)
 UND 00'''1'''0 (dezimal 2)
   = 00'''1'''0 (dezimal 2)

Da das Ergebnis 0010 ungleich Null ist, wissen wir, dass das zweite Bit im ursprünglichen Muster gesetzt war. Dies wird oft als „Bitmaskierung“ bezeichnet. (In Analogie dazu deckt oder „maskiert“ die Verwendung von [[Abdeckband]] Teile ab, die nicht geändert werden sollten, oder Teile, die nicht von Interesse sind. In diesem Fall maskieren die 0-Werte die Bits, die nicht von Interesse sind Interesse.)

Das bitweise UND kann verwendet werden, um ausgewählte Bits (oder [[Merkerwort|Merker]]) eines Registers zu löschen, in dem jedes Bit einen individuellen [[Boolescher Datentyp|Boolean]]-Zustand darstellt. Diese Technik ist eine effiziente Möglichkeit, eine Reihe von booleschen Werten zu speichern, wobei so wenig Speicherplatz wie möglich verwendet wird.

Beispielsweise kann 0110 (dezimal 6) als ein Satz von vier Flags betrachtet werden, wobei das erste und vierte Flag gelöscht (0) und das zweite und dritte Flag gesetzt (1) sind. Das dritte Flag kann gelöscht werden, indem ein bitweises UND mit dem Muster verwendet wird, das nur im dritten Bit eine Null enthält:

     0'''1'''10 (Dezimal 6)
 UND 1'''0'''11 (dezimal 11)
   = 0'''0'''10 (dezimal 2)

Aufgrund dieser Eigenschaft wird es einfach, die [[Parität (Mathematik)|Parität]] einer Binärzahl zu überprüfen, indem der Wert des niedrigstwertigen Bits überprüft wird. Anhand des obigen Beispiels:

     0110 (dezimal 6)
 UND 0001 (dezimal 1)
   = 0000 (dezimal 0)

Da 6 UND 1 null ist, ist 6 durch zwei teilbar und daher gerade.
