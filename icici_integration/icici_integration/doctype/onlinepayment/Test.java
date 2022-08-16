import com.fiserv.fdc.FDConnectUtils;
import com.fiserv.fdc.inquiry.model.FDConnectInquiryRequest;
import com.fiserv.fdc.inquiry.model.FDConnectInquiryResponse;
import com.google.gson.Gson;

public class Test {
        public static void main(String[] args) {
        //Using Constructor

            FDConnectInquiryRequest firstPayInquiryRequest =
                    new  FDConnectInquiryRequest("470000012765500",
                            "myak+AZNujouXgWnVdbteXqTfGXio3oB8/yHD7mSVKw=",
                            "3lOcRGUBshREdoV8dhWv5g==",
                            "https://test.fdconnect.com/FirstPayL2Services/getTxnInquiryDetail",
                            "OPP000192",
                            "");

            FDConnectInquiryResponse resp = FDConnectUtils.inquiryTxn(firstPayInquiryRequest);
            String inquiryStatus= new Gson().toJson(resp);
            System.out.println(inquiryStatus);
        }
}


