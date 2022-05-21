=====Kreisverschiebungen=====
{{Anker|Zirkuläre Verschiebungen in Sprachen der C-Familie}}
Der C-Sprachfamilie fehlt ein Rotationsoperator (obwohl C++20 <code>std::rotl</code> und <code>std::rotr</code> bereitstellt), aber einer kann aus der Verschiebung synthetisiert werden Betreiber. Es muss darauf geachtet werden, dass die Anweisung wohlgeformt ist, um [[undefiniertes Verhalten]] und [[Timing-Angriffe]] in Software mit Sicherheitsanforderungen zu vermeiden.<ref name="StackOverflow">{{cite web|url=https: //stackoverflow.com/q/31387778|title=Nahezu konstante Zeitrotation, die nicht gegen die Standards verstößt?|access-date=12. August 2015|publisher=Stack Exchange Network}}</ref> Zum Beispiel eine naive Implementierung, die Linksrotiert einen 32-Bit-Wert ohne Vorzeichen <code>x</code> um <code>n</code> Positionen ist einfach
<syntaxhighlight lang="c">
uint32_t x = ..., n = ...;
uint32_t y = (x << n) | (x >> (32 - n));
</syntaxhighlight>

Eine Verschiebung um <code>0</code> Bits führt jedoch zu undefiniertem Verhalten im rechten Ausdruck <code>(x >> (32 - n))</code>, weil <code>32 - 0</ code> ist <code>32</code> und <code>32</code> liegt außerhalb des Bereichs von 0–31 einschließlich. Ein zweiter Versuch könnte dazu führen
<syntaxhighlightlang="c">
uint32_t x = ..., n = ...;
uint32_t y = n ? (x << n) | (x >> (32 - n)): x;
</syntaxhighlight>
wo der Verschiebungsbetrag getestet wird, um sicherzustellen, dass er kein undefiniertes Verhalten einführt. Die Verzweigung fügt jedoch einen zusätzlichen Codepfad hinzu und bietet eine Gelegenheit für Timing-Analysen und Angriffe, was bei Software mit hoher Integrität oft nicht akzeptabel ist.<ref name="StackOverflow" /> Außerdem wird der Code zu mehreren Maschinenanweisungen kompiliert, was oft weniger effizient ist als die native Anweisung des Prozessors.

Um das undefinierte Verhalten und die Verzweigungen unter [[GNU Compiler Collection|GCC]] und [[Clang]] zu vermeiden, wird Folgendes empfohlen. Das Muster wird von vielen Compilern erkannt, und der Compiler gibt eine einzelne Rotationsanweisung aus:<ref>{{cite web|url=https://gcc.gnu.org/bugzilla/show_bug.cgi?id=57157|title= Schlechte Optimierung des portablen Rotate-Idioms|Zugriffsdatum=11. August 2015|Publisher=GNU GCC-Projekt}}</ref><ref>{{cite web|url=https://software.intel.com/en-us/ forums/topic/580884|title=Kreisrotation, die nicht gegen den C/C++-Standard verstößt?|access-date=12. August 2015|publisher=Intel Developer Forums}}</ref><ref name=LLVM>{{cite web| url=https://llvm.org/bugs/show_bug.cgi?id=24226|title=Konstante nicht in Inline-Assembly weitergegeben, führt zu &quot;Einschränkung 'I' erwartet einen ganzzahligen konstanten Ausdruck&quot;|access-date=11 August 2015|publisher=LLVM-Projekt}}</ref>
<syntaxhighlight lang="c">
uint32_t x = ..., n = ...;
uint32_t y = (x << n) | (x >> (-n & 31));
</syntaxhighlight>

Es gibt auch Compiler-spezifische [[Intrinsic Function|Intrinsics]], die [[Circular Shift]]s implementieren, wie [http://msdn.microsoft.com/en-us/library/t5e2f3sc(VS.80).aspx _rotl8 , _rotl16], [http://msdn.microsoft.com/en-us/library/yy0728bz(VS.80).aspx _rotr8, _rotr16] in Microsoft [[Visual C++]]. Clang bietet einige intrinsische Rotationsfunktionen für Microsoft-Kompatibilität, die unter den oben genannten Problemen leiden. <ref name=LLVM /> GCC bietet keine intrinsischen Rotationsfunktionen. Intel bietet auch x86 an [https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=rot&techs=Other intrinsics].
