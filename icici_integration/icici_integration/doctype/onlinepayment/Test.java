import com.fiserv.fdc.FDConnectUtils;
import com.fiserv.fdc.inquiry.model.FDConnectInquiryRequest;
import com.fiserv.fdc.inquiry.model.FDConnectInquiryResponse;
import com.fiserv.fdc.sale.model.FDConnectSaleRequest;
import com.fiserv.fdc.sale.model.FDConnectSaleResponse;
import com.fiserv.fdc.response.model.FDConnectDecryptRequest;
import com.fiserv.fdc.response.model.FDConnectDecryptResponse;
import com.google.gson.Gson;

public class Test {
        public static void main(String[] args) {
                //  FDConnectSaleRequest request = new FDConnectSaleRequest("470000012765500",
                // "myak+AZNujouXgWnVdbteXqTfGXio3oB8/yHD7mSVKw=","3lOcRGUBshREdoV8dhWv5g==",
                // " https://test.fdconnect.com/FirstPayL2Services/getToken",
                // "10","INR","4rerf","sale",
                // "http://localhost:8080");

                // FDConnectSaleResponse resp = FDConnectUtils.saleTxn(request);
                // System.out.println("resp SessionTokenId :" + resp.getSessionTokenId());
                // System.out.println("respErrorCode :"+resp.getErrorCode());
                // System.out.println("ErrorMessage :"+resp.getErrorMessage());



        //Using Constructor

        //     FDConnectInquiryRequest firstPayInquiryRequest =
        //             new  FDConnectInquiryRequest("470000012765500",
        //                     "myak+AZNujouXgWnVdbteXqTfGXio3oB8/yHD7mSVKw=",
        //                     "3lOcRGUBshREdoV8dhWv5g==",
        //                     "https://test.fdconnect.com/FirstPayL2Services/getTxnInquiryDetail",
        //                     "OPP000192",
        //                     "");
        //     FDConnectInquiryResponse resp = FDConnectUtils.inquiryTxn(firstPayInquiryRequest);
        //     String inquiryStatus= new Gson().toJson(resp);
        //     System.out.println(inquiryStatus);
         


          FDConnectDecryptRequest fdConnectDecryptRequest = new FDConnectDecryptRequest("470000012765500",
                        "h2sUPU86ytjDciY1EEAPceGB9NqBD0eBJXzoBQVfQlTNmuquLkkt6DpiqmVPVyJszr4i98qR87jmWd3rMFvpTKZQ9r52zaWb+kUUN/URzKKJhkjqmuGaGVWyUvwwraoXq8I5k7xlvKORJ9AwOFnyP//y3c0ozcavVkOhpVJ0ECGnpq/PSzW7DJvDRC8NiRRo18k4qiyuw6iyg/FUjRXNd/il2zKO8Li/BtDV7zYabRfilY0XsSKapu67BReOJPe6+jB+EKpE54OzUGqv+3apFxSkLLfti+rpX4sKbajOBfP73qUEbe8kzlZJnFcDXFhNJQmUSHZ1w8nt42fI2f8illKcPpfmAYb3w8EzhDd0fYJXPxUUTypiLp5lCGCTg2tppYpLbuXdF5lz8HNnLVH3ctNFAow2m+8bK7EFkTWyZm0nmFJ4fNBwIQfGhZHMOXBjyyClviMYvYeiGa2/+Rbdztz5CvhxVvvFsQQmfEcj4vXrg/2OCiy6wfZhtInB0b4WYmYfoYGqB0aolZdgWUTIL6AxsyTGha9CeK8r0AWXRz5VtIxmzL5HKJb+qZpRWVH1Id/shS4KW1AZpaUN50vqfoFvQrESqcNI2nt1gFzsse9opeT+B2Jn+mw1Tqbydqg/LukiUuNTIayeYa/3GYphMhFUNEyZeaPR5h6wgOqyadreSo3VffHkkrarV5D7+OR3j55YbtZDBwrFunU3Sv2+Rs9U5KHvvHedUaxUK37Rdj5tUM4+gVx7ZOvHnl2wOwW0J6ixHExssalp5zJoRHF5pIWOjOSKraM50QiqCDBPgTtPXR3RzcOZYrFOmhdy92wfC/1M3kjGcm2LolAe6tnjRYmtPSNfBAwtWfeEsiXEZWe4ugp/VN4sQrPkrhpO0Y1L6hZzwhXF/jqnBC+Ax5/kWfKhqSP7VTjRNS0Sl2gcMrm0MkZnpYBu2oQEbmLyz4V+",
                "2022080959113800","https://test.fdconnect.com/FirstPayL2Services/decryptMerchantResponse");

        FDConnectDecryptResponse resp = FDConnectUtils.decryptMsg(fdConnectDecryptRequest);
        //   System.out.println(FDConnectUtils.decryptMsg(fdConnectDecryptRequest));
        //   System.out.println(new Gson().toJson(resp));
          String dR=new Gson().toJson(resp);
          System.out.println(dR);


        
          
        }
}



