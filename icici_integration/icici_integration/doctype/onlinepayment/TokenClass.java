import com.fiserv.fdc.FDConnectUtils;
import com.fiserv.fdc.sale.model.FDConnectSaleRequest;
import com.fiserv.fdc.sale.model.FDConnectSaleResponse;
import com.fiserv.fdc.response.model.FDConnectDecryptRequest;
import com.fiserv.fdc.response.model.FDConnectDecryptResponse;
import com.google.gson.Gson;
import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;

public class TokenClass {

    public static String getToken(String merchantId, String key, String iv, String apiURL, String amount, String currencyCode, String merchantTxnId, String transactionType, String resultURL) throws IOException {
        
        FDConnectSaleRequest request = new FDConnectSaleRequest(merchantId,key,iv,apiURL,amount,currencyCode,merchantTxnId,transactionType,resultURL);
        FDConnectSaleResponse resp = FDConnectUtils.saleTxn(request);

        System.out.println("resp SessionTokenId :" + resp.getSessionTokenId());
        System.out.println("respErrorCode :"+resp.getErrorCode());
        System.out.println("ErrorMessage :"+resp.getErrorMessage());  
        
        String tokenId=resp.getSessionTokenId();
        return tokenId;
    }
   
    public static String getDecryptResponse(String merchantId,String encData,String fdcTxnId,String apiURL) throws IOException {
        
            FDConnectDecryptRequest fdConnectDecryptRequest = new FDConnectDecryptRequest(merchantId,encData,fdcTxnId,apiURL);
            FDConnectDecryptResponse resp = FDConnectUtils.decryptMsg(fdConnectDecryptRequest);
    
            System.out.println(resp.getErrorCode());
            System.out.println(resp.getErrorMessage());
            System.out.println(new Gson().toJson(resp));

            String decData=resp.getTransactionStatus();
            return decData;
    }
}


   