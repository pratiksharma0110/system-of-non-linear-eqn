root = csvread("results.csv"); 

fid = fopen("metadata.txt", "r");
if fid == -1
    error("metadata.txt not found.");
end

fgetl(fid); 
variables_line = fgetl(fid);
variables = strsplit(variables_line, ", ");

fgetl(fid); 
eqn1_str = fgetl(fid); 
eqn2_str = fgetl(fid); 
fclose(fid);

eqn1 = @(x, y) eval(eqn1_str);
eqn2 = @(x, y) eval(eqn2_str);

if length(variables) == 2
    x = linspace(-10, 10, 100); 
    y = linspace(-10, 10, 100);
    [X, Y] = meshgrid(x, y);

    Z1 = arrayfun(eqn1, X, Y);
    Z2 = arrayfun(eqn2, X, Y);

    contour(X, Y, Z1, [0 0], 'r', 'LineWidth', 2); hold on;
    contour(X, Y, Z2, [0 0], 'b', 'LineWidth', 2); hold on;

    plot(root(1), root(2), 'ko', 'MarkerFaceColor', 'g', 'MarkerSize', 8);

    text(root(1), root(2) + 1, sprintf("Root: (%.4f, %.4f)", root(1), root(2)), ...
         'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center', ...
         'FontSize', 10, 'Color', 'k');

    grid on; 
    ax = gca;
    ax.XMinorGrid = 'on';
    ax.YMinorGrid = 'on'; 
    ax.MinorGridLineStyle = ':'; 
    ax.GridLineStyle = '--'; 

    axis equal;

    title("Solution of Nonlinear Equations", 'FontWeight', 'bold', 'FontSize', 14); 
    xlabel("x-axis", 'FontWeight', 'bold', 'FontSize', 12); 
    ylabel("y-axis", 'FontWeight', 'bold', 'FontSize', 12); 
    legend("Equation 1", "Equation 2", "Root", 'Location', 'best');
    hold off;

else
    disp("Plotting for more than 2 variables is not supported in this script.");
end
