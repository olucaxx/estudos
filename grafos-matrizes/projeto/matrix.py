from typing import Iterable

class Matrix():
    def __init__(self, nrow: int, ncol: int, byrow: bool = False, dimnames: list[list[str]] | None = None, data: Iterable[int | float] | None = None):
        self.nrow = nrow
        self.ncol = ncol
        self.dim = nrow, ncol
        
        self.values = self.__set_values(data, byrow)
        self.dimnames = None
        
        if dimnames:
            # precisa ter a quantidade correta de nomes para as linhas e colunas
            if len(dimnames[0]) != nrow:
                raise ValueError(f"length of 'dimnames' [1] not equal to array extent")
            if len(dimnames[1]) != ncol:
                raise ValueError(f"length of 'dimnames' [2] not equal to array extent")
            
            self.dimnames = dimnames
                
                
    def __set_values(self, data: Iterable[int | float], byrow: bool) -> list[list[int | float]]:
        # inicia a lista com os valores todos None
        values = [[None for _ in range(self.ncol)] for _ in range(self.nrow)]
        
        # se não for informado os valores, retorna a lista vazia mesmo
        if not data:
            return values
        
        data = list(data)
        
        # verificar se os valores de 'data' conseguem ser encaixados na matriz
        if len(data) % self.nrow != 0:
            raise ValueError(f"data length [{len(data)}] is not a sub-multiple or multiple of the number of rows [{self.nrow}]")
        if len(data) % self.ncol != 0:
            raise ValueError(f"data length [{len(data)}] is not a sub-multiple or multiple of the number of columns [{self.ncol}]")
        
        # organiza os valores indo de coluna em coluna
        if not byrow:
            for i in range(self.ncol):
                for j in range(self.nrow):
                    values[j][i] = data.pop(0)
            return values
        
        # organiza os valores indo de linha em linha
        for i in range(self.nrow):
            for j in range(self.ncol):
                values[i][j] = data.pop(0)
        return values
    
    
    def __getitem__(self, indexes: tuple[int | str, int | str]) -> int | float | None:
        i, j = indexes
        
        if isinstance(i, str):
            try:
                i = self.dimnames[0].index(i)
            except ValueError:
                raise IndexError(f"row '{i}' out of bounds")
         
        if isinstance(j, str):
            try:
                j = self.dimnames[1].index(j)
            except ValueError:
                raise IndexError(f"column '{j}' out of bounds") 
           
        if isinstance(i, int):
            if i < 0 or i >= self.nrow:
                raise IndexError(f"index [{i}] out of bounds")
            
        if isinstance(j, int):
            if j < 0 or j >= self.ncol:
                raise IndexError(f"index [{j}] out of bounds")
            
        return self.values[i][j]
        
    
    def __setitem__(self, indexes: tuple[int | str, int | str], value: int | float) -> None:
        i, j = indexes
        
        if isinstance(i, str):
            try:
                i = self.dimnames[0].index(i)
            except ValueError:
                raise IndexError(f"row '{i}' out of bounds")
         
        if isinstance(j, str):
            try:
                j = self.dimnames[1].index(j)
            except ValueError:
                raise IndexError(f"column '{j}' out of bounds") 
           
        if isinstance(i, int):
            if i < 0 or i >= self.nrow:
                raise IndexError(f"index [{i}] out of bounds")
            
        if isinstance(j, int):
            if j < 0 or j >= self.ncol:
                raise IndexError(f"index [{j}] out of bounds")
        
        self.values[i][j] = value
            
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.dim != other.dim:
            raise ValueError("matrixes dimesions not equal")
        
        result_data = [self.values[i][j] + other.values[i][j] for j in range(self.ncol) for i in range(self.nrow)]
        
        return Matrix(nrow=self.nrow, ncol=self.ncol, data=result_data, dimnames=self.dimnames)
    
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if self.dim != other.dim:
            raise ValueError("matrixes dimesions not equal")
        
        result_data = [self.values[i][j] - other.values[i][j] for j in range(self.ncol) for i in range(self.nrow)]
        
        return Matrix(nrow=self.nrow, ncol=self.ncol, data=result_data, dimnames=self.dimnames)
    
    
    def __mul__(self, other: 'Matrix | int | float') -> 'Matrix':
        if isinstance(other, (int, float)):
            result_data = [
                self.values[i][j] * other for j in range(self.ncol)
                for i in range(self.nrow)
            ]
            return Matrix(nrow=self.nrow, ncol=self.ncol, data=result_data, dimnames=self.dimnames)
        
        if self.ncol != other.nrow:
            raise ValueError("invalid matrixes dimensions")
        
        result_data = [
            sum([self.values[i][k] * other.values[k][j] for k in range(self.ncol)]) 
            for j in range(other.ncol) 
            for i in range(self.nrow)
            ] 
        
        if other.dimnames and self.dimnames:
            return Matrix(nrow=self.nrow, ncol=other.ncol, data=result_data, dimnames=[self.dimnames[0], other.dimnames[1]])
        
        return Matrix(nrow=self.nrow, ncol=other.ncol, data=result_data)
            
            
    def __str__(self) -> str:
        # caso não seja informado os nomes paras as linhas e colunas, vamos gerar apenas os index delas
        if not self.dimnames:
            string = " "*4
            # colocar os números que indicam a coluna primeiro, como um cabeçalho
            for i in range(self.ncol):
                string += f"[,{i}]".rjust(7)
            string += "\n"
                
            for i in range(self.nrow):
                string += f"[{i},]"
                for item in self.values[i]:
                    string += f"{str(item):>7}"
                string += "\n"
            
            return string
        
        spacings = []
        row_name_spacing = max([len(i) for i in self.dimnames[0]])
        string = " " * row_name_spacing
        
        for item in self.dimnames[1]:
            item_length = len(item)
            value = 1
            if item_length < 7:
                value = 7 - item_length
                
            string += item.rjust(item_length + value)
            spacings.append(item_length + value)
        string += "\n"
            
        for i in range(len(self.dimnames[0])):
            string += str(self.dimnames[0][i]).ljust(row_name_spacing)
            
            for j in range(self.ncol):
                string += str(self.values[i][j]).rjust(spacings[j])
                
            string += "\n"
        
        return string
        
        
def main():
    matrizA = Matrix(data=[1,3,2,2,1,1], nrow=2, ncol=3, byrow=True)
    matrizB = Matrix(data=[2,1,3,1,0,2,1,1,0], nrow=3, ncol=3, byrow=True)
    print(matrizA * matrizB)
       
       
if __name__ == "__main__":
    main()
