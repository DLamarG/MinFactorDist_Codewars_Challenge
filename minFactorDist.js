function minDistance(n){
    let factors = []
    let minDist = n
  
    for (let i = 1; i <= n; i++) {
      if (n % i === 0) {
        factors.push(i)
      }
    }
  
    for (let i = 0; i < factors.length - 1; i++) {
      if (factors[i + 1] - factors[i] < minDist) {
        minDist = factors[i + 1] - factors[i]
      }
    }
    return minDist
  }


console.log(minDistance(8))
console.log(minDistance(25))
console.log(minDistance(13013))