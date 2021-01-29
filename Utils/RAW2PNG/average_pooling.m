function P = average_pooling(data, kernal)
len = size(data, 2);
P = zeros(len/kernal, len/kernal);
for i=1:len/kernal
    for j=1:len/kernal
        i_st = (i-1)*kernal+1;
        i_ed = i_st+kernal-1;
        j_st = (j-1)*kernal+1;
        j_ed = j_st+kernal-1;
        P(i,j) = mean(mean(abs(data( 1, i_st:i_ed, j_st:j_ed)).^2+abs(data( 2, i_st:i_ed, j_st:j_ed)).^2));
    end
end