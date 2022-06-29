import javax.imageio.ImageIO;
import java.io.File;
// import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.lang.Math;
// import java.lang.Integer;

public class Cvert {
    public static void main(String[] args) {
        try {
            File file = new File(args[0]);
            BufferedImage image = ImageIO.read(file);
            double wid = Math.ceil(image.getWidth() / 3);
            double heg = Math.ceil(image.getHeight() / 3);
            BufferedImage res = new BufferedImage((int)wid, (int)heg, image.getType());

            for (int x = 0;  x < res.getWidth(); x++) {
                for (int y = 0; y < res.getHeight(); y++) {
                    res.setRGB(x, y, image.getRGB(x * 3, y * 3));
                }
            }

            int[][] znach = {
                {0, 0, 0}, 
                {0, 0, 0}, 
                {0, 0, 0}
            };

            // int k = 0;
            // while (k < 11) {
                // System.out.println("Iteretion: " + k);
                // k++;
                for (int x = 0;  x < res.getWidth(); x++) {
                    for (int y = 0; y < res.getHeight(); y++) {
                        if (
                            (y > 0 & y < res.getHeight()) &
                            (x < 0 & x < res.getWidth())
                        ) {
                            znach[0][0] = res.getRGB(x - 1, y - 1);
                            znach[0][1] = res.getRGB(x - 1, y);
                            znach[0][2] = res.getRGB(x - 1, y + 1);

                            znach[1][0] = res.getRGB(x, y - 1);
                            znach[1][1] = res.getRGB(x, y);
                            znach[1][2] = res.getRGB(x, y + 1);

                            znach[2][0] = res.getRGB(x + 1, y - 1);
                            znach[2][1] = res.getRGB(x + 1, y);
                            znach[2][1] = res.getRGB(x + 1, y + 1);
                        }
                    }
                    
                    for (int xx = 0;  xx < 3; xx++) {
                        for (int yy = 0; yy < 3; yy++) {
                            if (yy < 2) {
                                System.out.print(znach[xx][yy]);
                            } else {
                                System.out.println(znach[xx][yy]);
                            }
                        }
                    }
                }

            // }

            File cvert = new File("cvert.jpg");
            ImageIO.write(res, "jpg", cvert);

        } catch (IOException e) {
            System.out.println("Can't read or save");
        }
    }
}