/**
 * @input X : Integer array corresponding to the X co-ordinate
 * @input n1 : Integer array's ( X ) length
 * @input Y : Integer array corresponding to the Y co-ordinate
 * @input n2 : Integer array's ( Y ) length
 *
 * Points are represented by (X[i], Y[i])
 * 
 * @Output Integer
 *
 */
int coverPoints(int* X, int n1, int* Y, int n2) {
    int i;
    int stepx=0,stepy=0,tsteps = 0;
    for(i = 1; i < n1;i++){
        
        stepx = X[i]-X[i-1];
        
        stepy = Y[i]-Y[i-1];
        
        if(stepx < 0){
            stepx *= -1;
        }
        if(stepy < 0){
            stepy *= -1;
        }
        
        if (stepx > stepy) {
            tsteps += stepx;
        } else {
            tsteps += stepy;
        }
        
    }
    return tsteps;
}
